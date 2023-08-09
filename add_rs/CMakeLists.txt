cmake_minimum_required(VERSION 3.0)
project(add_rs)

# Find and include Conan dependencies
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Build Rust library
add_custom_target(rust_build ALL
    COMMAND cargo build --release
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)
