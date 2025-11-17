import os
import shutil
import subprocess
import tempfile

from setuptools.command.build_py import build_py


class GnuplotBuild(build_py):
    """Custom build command to build and install gnuplot."""

    def run(self):
        gnuplot_dir = "gnuplot-main"
        if not os.path.exists(gnuplot_dir):
            raise RuntimeError("gnuplot source directory not found")

        # The installation directory for gnuplot, within the package
        install_dir = os.path.abspath(
            os.path.join(self.build_lib, "gnuplot_wheel", "bin")
        )
        os.makedirs(install_dir, exist_ok=True)

        # Temporary directory for installation
        with tempfile.TemporaryDirectory() as tmpdir:
            dest_dir = os.path.join(tmpdir, "gnuplot_install")
            os.makedirs(dest_dir, exist_ok=True)

            # Run ./prepare if configure does not exist
            if not os.path.exists(os.path.join(gnuplot_dir, "configure")):
                subprocess.check_call(["./prepare"], cwd=gnuplot_dir)

            # Configure, make, and install
            prefix = "/usr/local"
            configure_command = [
                "./configure",
                f"--prefix={prefix}",
                "--without-qt",
                "--without-wx",
                "--without-lua",
                "--without-libcerf",
            ]
            subprocess.check_call(configure_command, cwd=gnuplot_dir)
            subprocess.check_call(["make"], cwd=gnuplot_dir)
            subprocess.check_call(
                ["make", "install", f"DESTDIR={dest_dir}"], cwd=gnuplot_dir
            )

            # Copy the gnuplot binary to the package
            shutil.copy(
                os.path.join(dest_dir, prefix.lstrip("/"), "bin", "gnuplot"),
                install_dir,
            )

        super().run()
