# Cargo Add

simple tool to add crates to your Cargo.toml file.
-



## setup:

in a bash shell run:

```bash
    cd && git clone https://github.com/0Atticus/cargo-add && function add { python3 ~/cargo-add/main.py $1 $(readlink -f Cargo.toml) }
```

to use:
-
in your cargo folder run:

```bash
add [crate name]
```
to add the latest version of the crate to your dependencies

