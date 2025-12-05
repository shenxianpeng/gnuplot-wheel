# Set up Build Dependencies

A reusable composite action that installs platform-specific build dependencies required for building gnuplot from source.

## What it does

This action automatically detects the runner OS and installs the appropriate build dependencies by calling shell scripts located in `.github/scripts/`.

### macOS
Runs `setup-macos.sh` which installs:
- autoconf
- automake
- libtool
- gd
- jpeg

### Linux
Runs `setup-linux.sh` which automatically detects the package manager and installs dependencies:

**For apt-get (Debian/Ubuntu):**
- libgd-dev
- libreadline-dev
- libpng-dev
- zlib1g-dev
- libjpeg-dev
- libfreetype6-dev
- libfontconfig1-dev

**For yum (RHEL/CentOS):**
- readline-devel
- libpng-devel
- zlib-devel
- libjpeg-devel
- freetype-devel
- fontconfig-devel
- libgd (built from source with FreeType support)

### Windows
No dependencies are installed on Windows (uses pre-built binaries).

## Usage in Workflows

### As a Composite Action

```yaml
steps:
  - uses: actions/checkout@v6
  
  - name: Set up build dependencies
    uses: ./.github/actions/setup-build-deps
```

### As Shell Scripts (e.g., in cibuildwheel)

The same scripts used by the composite action can be called directly:

```yaml
- name: Build wheels
  uses: pypa/cibuildwheel@v3.3
  env:
    CIBW_BEFORE_ALL_LINUX: bash .github/scripts/setup-linux.sh
    CIBW_BEFORE_ALL_MACOS: bash .github/scripts/setup-macos.sh
```

## Scripts

The actual dependency installation logic is in these shell scripts:
- `.github/scripts/setup-macos.sh` - macOS dependencies
- `.github/scripts/setup-linux.sh` - Linux dependencies (supports both apt-get and yum)

This approach allows the same dependency installation logic to be reused across different workflows, including those that use cibuildwheel.

## Requirements

- Requires the repository to be checked out first
- Works on ubuntu-latest, macos-latest, and windows-latest runners
- Scripts are automatically made executable
