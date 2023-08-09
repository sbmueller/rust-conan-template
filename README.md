# Rust Conan Template

This repository is a proof of concept (PoC) on

1. How to write a library in Rust and offer an interface to C/C++
2. How to wrap a Rust library in a Conan package
3. How to use a Conan wrapped Rust library from a C++ application

The repository consists of two Conan packages.

- `add_rs` is a library written in Rust, that offers adding two integers via
  its public interface
- `add_cpp` is a C++ application that adds two numbers, making use of `add_rs`
