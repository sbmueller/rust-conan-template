from conans import ConanFile, CMake


class AddRsConan(ConanFile):
    name = "add_rs"
    version = "1.0"
    author = "Sebastian Müller"
    description = "Rust library to add two integers"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = (
        "src/*",
        "include/*",
        "CMakeLists.txt",
        "Cargo.toml",
        "build.rs",
    )

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build(target="rust_build")  # Build the Rust library

    def package(self):
        # On MacOS
        self.copy("*.dylib", src="target/release", dst="lib", keep_path=False)
        # On Linux
        self.copy("*.so", src="target/release", dst="lib", keep_path=False)
        self.copy("*.h", src="include", dst="include")  # Include the header file

    def package_info(self):
        self.cpp_info.libs = [self.name]
