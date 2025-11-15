
import sys
from setuptools import setup, find_packages

sys.path.insert(0, '.')
from build import GnuplotBuild

setup(
    name='gnuplot_wheel',
    version='0.0.1',
    packages=find_packages(),
    cmdclass={
        'build_py': GnuplotBuild,
    },
    package_data={
        'gnuplot_wheel': ['bin/gnuplot'],
    },
)
