
import sys
from setuptools import setup, find_packages
from setuptools.command.bdist_wheel import bdist_wheel as _bdist_wheel

sys.path.insert(0, '.')
from build import GnuplotBuild

class custom_bdist_wheel(_bdist_wheel):
    def run(self):
        self.run_command('build_py')
        super().run()

setup(
    name='gnuplot_wheel',
    version='0.0.1',
    packages=find_packages(),
    cmdclass={
        'build_py': GnuplotBuild,
        'bdist_wheel': custom_bdist_wheel,
    },
    package_data={
        'gnuplot_wheel': ['bin/gnuplot'],
    },
)
