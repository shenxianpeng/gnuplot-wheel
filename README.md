# gnuplot

[![PyPI](https://img.shields.io/pypi/v/gnuplot-wheel.svg)](https://pypi.org/project/gnuplot-wheel/)
[![Python](https://img.shields.io/pypi/pyversions/gnuplot-wheel.svg)](https://pypi.org/project/gnuplot-wheel/)
[![main](https://github.com/shenxianpeng/gnuplot-wheel/actions/workflows/main.yml/badge.svg)](https://github.com/shenxianpeng/gnuplot-wheel/actions/workflows/main.yml)

A Python wheel distribution of [gnuplot](http://gnuplot.info/) - install and use gnuplot directly via pip.

## Installation

```bash
pip install gnuplot-wheel
```

## Development

```bash
git clone --recursive https://github.com/shenxianpeng/gnuplot-wheel.git
cd gnuplot-wheel
python3 -m build --wheel
pip install dist/gnuplot-*.whl
```

## License

MIT License. Gnuplot itself has its own license - see [gnuplot.info](http://gnuplot.info/).
