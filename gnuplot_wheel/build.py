import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile

from setuptools.command.build_py import build_py


class GnuplotBuild(build_py):
    """Custom build command to build and install gnuplot."""

    def run(self):
        # The installation directory for gnuplot, within the package
        install_dir = os.path.abspath(
            os.path.join(self.build_lib, "gnuplot_wheel", "bin")
        )
        os.makedirs(install_dir, exist_ok=True)

        if sys.platform == "win32":
            # Download pre-built Windows binary
            self._build_windows(install_dir)
        else:
            # Build from source on Linux/macOS
            self._build_unix(install_dir)

        super().run()

    def _build_windows(self, install_dir):
        """Download and extract pre-built Windows gnuplot binary."""
        print("Downloading gnuplot for Windows...")

        # Get gnuplot version from environment or use default
        gnuplot_version = os.environ.get("GNUPLOT_VERSION", "6.0.1")
        version_short = gnuplot_version.replace(".", "")

        # Use the official gnuplot Windows binary
        url = f"https://sourceforge.net/projects/gnuplot/files/gnuplot/{gnuplot_version}/gp{version_short}-win64-mingw.zip/download"

        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = os.path.join(tmpdir, "gnuplot.zip")

            # Download
            print(f"Downloading from {url}")
            urllib.request.urlretrieve(url, zip_path)

            # Extract
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(tmpdir)

            # Find and copy gnuplot.exe
            for root, dirs, files in os.walk(tmpdir):
                if "gnuplot.exe" in files:
                    src = os.path.join(root, "gnuplot.exe")
                    shutil.copy(src, install_dir)
                    print(f"Copied gnuplot.exe to {install_dir}")
                    return

            raise RuntimeError("Could not find gnuplot.exe in downloaded archive")

    def _build_unix(self, install_dir):
        """Build gnuplot from source on Unix-like systems."""
        gnuplot_version = os.environ.get("GNUPLOT_VERSION", "6.0.1")
        gnuplot_tag = os.environ.get("GNUPLOT_TAG", gnuplot_version)

        with tempfile.TemporaryDirectory() as tmpdir:
            gnuplot_dir = os.path.join(tmpdir, "gnuplot")

            # Clone specific tag from gnuplot repository
            print(f"Cloning gnuplot {gnuplot_tag}...")
            subprocess.check_call(
                [
                    "git",
                    "clone",
                    "--depth",
                    "1",
                    "--branch",
                    gnuplot_tag,
                    "https://git.code.sf.net/p/gnuplot/gnuplot-main",
                    gnuplot_dir,
                ]
            )

            dest_dir = os.path.join(tmpdir, "gnuplot_install")
            os.makedirs(dest_dir, exist_ok=True)

            # Run ./prepare to generate configure script
            if not os.path.exists(os.path.join(gnuplot_dir, "configure")):
                print("Running ./prepare...")
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
            print("Configuring gnuplot...")
            subprocess.check_call(configure_command, cwd=gnuplot_dir)

            print("Building gnuplot...")
            subprocess.check_call(["make", "-j4"], cwd=gnuplot_dir)

            print("Installing gnuplot...")
            subprocess.check_call(
                ["make", "install", f"DESTDIR={dest_dir}"], cwd=gnuplot_dir
            )

            # Copy the gnuplot binary to the package
            src_binary = os.path.join(dest_dir, prefix.lstrip("/"), "bin", "gnuplot")
            shutil.copy(src_binary, install_dir)
            print(f"Copied gnuplot binary to {install_dir}")
