import sys
from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py as _build_py

# Add the current directory to the path so we can import gnuplot_wheel
sys.path.insert(0, str(Path(__file__).parent.resolve()))

try:
    from gnuplot_wheel.build import GnuplotBuild

    cmdclass = {"build_py": GnuplotBuild}
except ImportError:
    # Fallback if the module isn't available yet
    cmdclass = {"build_py": _build_py}

setup(
    cmdclass=cmdclass,
)
