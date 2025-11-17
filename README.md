# gnuplot-wheel

[![CI](https://github.com/shenxianpeng/gnuplot-wheel/actions/workflows/ci.yml/badge.svg)](https://github.com/shenxianpeng/gnuplot-wheel/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/gnuplot-wheel.svg)](https://badge.fury.io/py/gnuplot-wheel)
[![Python Versions](https://img.shields.io/pypi/pyversions/gnuplot-wheel.svg)](https://pypi.org/project/gnuplot-wheel/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python wheel distribution of [gnuplot](http://gnuplot.info/), allowing you to install and use gnuplot directly as a Python package.

## Features

- 📦 Install gnuplot via pip - no system package manager needed
- 🔧 Self-contained binary - works out of the box
- 🐍 Python 3.8+ support
- 🍎 Cross-platform support (Linux, macOS)
- ✨ Modern Python packaging (pyproject.toml)

## Installation

Install from PyPI:

```bash
pip install gnuplot-wheel
```

Or using uv:

```bash
uv pip install gnuplot-wheel
```

After installation, the `gnuplot` command will be available in your environment:

```bash
gnuplot --version
```

## Usage

Simply use gnuplot as you normally would:

```bash
# Interactive mode
gnuplot

# Run a script
gnuplot my_plot.gp

# Inline command
gnuplot -e "plot sin(x)"
```

## Development

### Prerequisites

For building from source, you need:

**Ubuntu/Debian:**
```bash
sudo apt-get install build-essential autoconf automake libtool \
  libgd-dev libreadline-dev libpng-dev zlib1g-dev libjpeg-dev
```

**macOS:**
```bash
brew install autoconf automake libtool gd readline libpng jpeg
```

### Setup Development Environment

1. Clone the repository with submodules:
   ```bash
   git clone --recursive https://github.com/shenxianpeng/gnuplot-wheel.git
   cd gnuplot-wheel
   ```

2. Install uv (recommended):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Install development dependencies:
   ```bash
   uv pip install -e ".[dev]"
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Building

Build the wheel using uv:

```bash
uv pip install build setuptools-scm
python -m build
```

The built wheel will be in the `dist/` directory.

### Testing

Install the built wheel:

```bash
uv pip install dist/gnuplot_wheel-*.whl
gnuplot --version
```

### Code Quality

This project uses modern Python tooling:

- **black** - Code formatting
- **isort** - Import sorting
- **ruff** - Fast Python linting
- **mypy** - Static type checking
- **pre-commit** - Git hooks for quality checks

Run linters:

```bash
black gnuplot_wheel/
isort gnuplot_wheel/
ruff check gnuplot_wheel/
```

Or let pre-commit handle it:

```bash
pre-commit run --all-files
```

## CI/CD

This project uses GitHub Actions for:

- **CI**: Automated testing on multiple Python versions (3.8-3.12) and platforms (Ubuntu, macOS)
- **Release**: Automated building and publishing to PyPI on release

### Publishing to PyPI

1. Create a new release on GitHub
2. The release workflow will automatically build wheels and publish to PyPI
3. Configure PyPI trusted publishing in your repository settings

## Version Management

Versions are automatically managed by `setuptools-scm` based on git tags:

```bash
# Create a new version
git tag v0.1.0
git push --tags
```

## Project Structure

```
gnuplot-wheel/
├── gnuplot_wheel/
│   ├── __init__.py
│   ├── build.py          # Custom build logic
│   └── gnuplot_proxy.py  # Gnuplot wrapper script
├── gnuplot-main/         # Gnuplot source (submodule)
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
├── .pre-commit-config.yaml
├── pyproject.toml        # Modern Python project config
└── README.md
```

## License

MIT License - See LICENSE file for details.

Gnuplot itself is distributed under its own license. See the [gnuplot website](http://gnuplot.info/) for more information.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linters
5. Submit a pull request

## Links

- [PyPI Package](https://pypi.org/project/gnuplot-wheel/)
- [GitHub Repository](https://github.com/shenxianpeng/gnuplot-wheel)
- [Issue Tracker](https://github.com/shenxianpeng/gnuplot-wheel/issues)
- [Gnuplot Official Site](http://gnuplot.info/)
