# gnuplot-wheel

A Python wheel for gnuplot.

This project provides a Python wheel for gnuplot, allowing you to install gnuplot as a Python package.

## Installation

You can install the pre-built wheel from PyPI (once it's published):

```bash
pip install gnuplot-wheel
```

## Building from source

If you want to build the wheel from source, you'll need to have the necessary build tools for gnuplot on your system (e.g., a C++ compiler, make, etc.).

1.  Clone this repository:
    ```bash
    git clone https://github.com/shenxianpeng/gnuplot-wheel.git
    cd gnuplot-wheel
    ```

2.  Install the Python build tool:
    ```bash
    pip install build
    ```

3.  Build the wheel:
    ```bash
    python3 setup.py bdist_wheel
    ```

    The built wheel will be in the `dist/` directory. You can then install it with pip:
    ```bash
    pip install dist/gnuplot_wheel-*.whl
    ```