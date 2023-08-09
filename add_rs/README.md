# How To: Rust/C++ Bindings

## Make a Rust library accessible from C++

### Use the FFI

Rust relies on the Foreign Function Interface (FFI) to interface with other
languages. The FFI mainly targets C as language.

To make functions in Rust code accessible via the FFI, they need to be
externalized and declared as `no_mangle`:

```rust
// src/lib.rs

#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

- `extern "C"` ensures the C ABI is used for calling functions in shared
  libraries
- `#[no_mangle]` ensures the function names don't experience
  [mangling](https://en.wikipedia.org/wiki/Name_mangling)

### Build a dynamic library

By default, rust builds static libraries. To generate a dynamic library, the
`Cargo.toml` has to be extended by:

```toml
[lib]
crate-type   = ["cdylib"]
```

This ensures `rustc` actually compiles a dynamic library.

### Generate a C/C++ header file

To access functions in thirdparty libraries, C/C++ needs a header file that
declares the interface towards the library.

The header file can be generated automatically by using `cbindgen`. Add
`cbindgen` to the build dependencies in `Cargo.toml`:

```toml
[build-dependencies]
cbindgen = "0.24.3"
```

And place a custom `build.rs` file in the project root with the following
content:

```rust
extern crate cbindgen;

use std::env;

fn main() {
    let crate_dir = env::var("CARGO_MANIFEST_DIR").unwrap();
    println!("Generating C/C++ header");
    cbindgen::Builder::new()
      .with_crate(crate_dir)
      .generate()
      .expect("Unable to generate bindings")
      .write_to_file("include/mylib.h");
}
```

This will ensure when calling `cargo build`, `cbindgen` is used to
auto-generate a C/C++ header file that declares the interface of the Rust
library.
