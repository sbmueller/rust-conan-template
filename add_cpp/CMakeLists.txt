cmake_minimum_required(VERSION 3.0)
project(${CONAN_PACKAGE_NAME} VERSION ${CONAN_PACKAGE_VERSION})

# Find and include Conan dependencies
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${CONAN_PACKAGE_NAME} src/main.cpp)
target_link_libraries(${CONAN_PACKAGE_NAME} PRIVATE ${CONAN_LIBS})
