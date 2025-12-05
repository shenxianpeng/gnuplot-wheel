# Set up Build Dependencies

A reusable composite action that installs platform-specific build dependencies required for building gnuplot from source.

## What it does

This action automatically detects the runner OS and installs the appropriate build dependencies:

### macOS
- autoconf
- automake
- libtool
- gd
- jpeg

### Linux
- libgd-dev
- libreadline-dev
- libpng-dev
- zlib1g-dev
- libjpeg-dev
- libfreetype6-dev
- libfontconfig1-dev

### Windows
No dependencies are installed on Windows (uses pre-built binaries).

## Usage

```yaml
steps:
  - uses: actions/checkout@v6
  
  - name: Set up build dependencies
    uses: ./.github/actions/setup-build-deps
```

## Requirements

- Requires the repository to be checked out first (uses local action path)
- Works on ubuntu-latest, macos-latest, and windows-latest runners
