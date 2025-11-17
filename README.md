# gnuplot

[![PyPI](https://img.shields.io/pypi/v/gnuplot.svg)](https://pypi.org/project/gnuplot/)
[![Python](https://img.shields.io/pypi/pyversions/gnuplot.svg)](https://pypi.org/project/gnuplot/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python wheel distribution of [gnuplot](http://gnuplot.info/) - install and use gnuplot directly via pip.

## Installation

```bash
pip install gnuplot
```

## Usage

```bash
# Check version
gnuplot --version

# Interactive mode
gnuplot

# Run a script
gnuplot my_plot.gp

# Inline command
gnuplot -e "plot sin(x)"
```

## Development

### Prerequisites

**Ubuntu/Debian:**
```bash
sudo apt-get install build-essential autoconf automake libtool \
  libgd-dev libreadline-dev libpng-dev zlib1g-dev libjpeg-dev
```

**macOS:**
```bash
brew install autoconf automake libtool gd readline libpng jpeg
```

### Build from source

```bash
# Clone with submodules
git clone --recursive https://github.com/shenxianpeng/gnuplot-wheel.git
cd gnuplot-wheel

# Install in editable mode
pip install -e .

# Or build wheel
pip install build
python -m build
```

## License

MIT License. Gnuplot itself has its own license - see [gnuplot.info](http://gnuplot.info/).
