from conans import ConanFile, CMake


class MyCppProjectConan(ConanFile):
    name = "add_cpp"
    version = "1.0"
    author = "Sebastian Müller"
    description = "Executable that adds two numbers"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt"

    requires = "add_rs/1.0"  # rust library

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(self.name, src="bin", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = []
