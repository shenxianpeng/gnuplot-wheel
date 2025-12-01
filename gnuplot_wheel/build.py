import os
import re
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

        # Strip .postN suffix for SourceForge download (e.g., 6.0.0.post1 -> 6.0.0)
        gnuplot_base_version = re.sub(r"\.post\d+$", "", gnuplot_version)
        version_short = gnuplot_base_version.replace(".", "")

        # Use the official gnuplot Windows binary
        url = f"https://sourceforge.net/projects/gnuplot/files/gnuplot/{gnuplot_base_version}/gp{version_short}-win64-mingw.zip/download"

        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = os.path.join(tmpdir, "gnuplot.zip")

            # Download
            print(f"Downloading from {url}")
            urllib.request.urlretrieve(url, zip_path)

            # Extract
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(tmpdir)

            # Find the bin directory containing gnuplot.exe and all DLLs
            gnuplot_bin_dir = None
            for root, dirs, files in os.walk(tmpdir):
                if "gnuplot.exe" in files:
                    gnuplot_bin_dir = root
                    break

            if not gnuplot_bin_dir:
                raise RuntimeError("Could not find gnuplot.exe in downloaded archive")

            # Copy gnuplot.exe and all DLL files
            files_copied = 0
            for file in os.listdir(gnuplot_bin_dir):
                if file.lower().endswith((".exe", ".dll")):
                    src = os.path.join(gnuplot_bin_dir, file)
                    dst = os.path.join(install_dir, file)
                    shutil.copy(src, dst)
                    files_copied += 1
                    print(f"Copied {file} to {install_dir}")

            if files_copied == 0:
                raise RuntimeError("No executable or DLL files found")

            print(
                f"Successfully copied {files_copied} files (gnuplot.exe and dependencies)"
            )

    def _build_unix(self, install_dir):
        """Build gnuplot from source on Unix-like systems."""
        gnuplot_version = os.environ.get("GNUPLOT_VERSION", "6.0.1")
        gnuplot_tag = os.environ.get("GNUPLOT_TAG", gnuplot_version)

        # Strip .postN suffix from tag for cloning (e.g., 6.0.0.post1 -> 6.0.0)
        gnuplot_base_version = re.sub(r"\.post\d+$", "", gnuplot_tag)

        with tempfile.TemporaryDirectory() as tmpdir:
            gnuplot_dir = os.path.join(tmpdir, "gnuplot")

            # Clone specific tag from gnuplot repository
            print(f"Cloning gnuplot {gnuplot_base_version}...")
            subprocess.check_call(
                [
                    "git",
                    "clone",
                    "--depth",
                    "1",
                    "--branch",
                    gnuplot_base_version,
                    "https://git.code.sf.net/p/gnuplot/gnuplot-main",
                    gnuplot_dir,
                ]
            )

            # Run ./prepare to generate configure script
            if not os.path.exists(os.path.join(gnuplot_dir, "configure")):
                print("Running ./prepare...")
                subprocess.check_call(["./prepare"], cwd=gnuplot_dir)

            # Configure gnuplot build
            configure_command = [
                "./configure",
                "--without-qt",
                "--without-wx",
                "--without-lua",
                "--without-libcerf",
            ]
            print("Configuring gnuplot...")

            # Set locale to UTF-8 to handle multibyte characters in documentation
            build_env = os.environ.copy()
            build_env["LC_ALL"] = "en_US.UTF-8"
            build_env["LANG"] = "en_US.UTF-8"

            subprocess.check_call(configure_command, cwd=gnuplot_dir, env=build_env)

            print("Building gnuplot...")
            # Build only the gnuplot binary, skip docs to avoid locale issues
            subprocess.check_call(
                ["make", "-j4", "gnuplot"], cwd=gnuplot_dir, env=build_env
            )

            # Copy the gnuplot binary directly from the build directory
            src_binary = os.path.join(gnuplot_dir, "src", "gnuplot")
            if not os.path.exists(src_binary):
                # Fallback: try without src/ subdirectory
                src_binary = os.path.join(gnuplot_dir, "gnuplot")

            shutil.copy(src_binary, install_dir)
            print(f"Copied gnuplot binary to {install_dir}")
