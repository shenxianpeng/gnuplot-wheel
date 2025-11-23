import os
import subprocess
import sys


def main():
    """
    A proxy for the gnuplot executable.
    """
    # The path to the gnuplot executable will be relative to this script.
    # On Windows, we need to use gnuplot.exe
    bin_dir = os.path.join(os.path.dirname(__file__), "bin")

    if sys.platform == "win32":
        gnuplot_exe = os.path.join(bin_dir, "gnuplot.exe")
    else:
        gnuplot_exe = os.path.join(bin_dir, "gnuplot")

    if not os.path.exists(gnuplot_exe):
        print(f"Error: gnuplot executable not found at {gnuplot_exe}", file=sys.stderr)
        sys.exit(1)

    try:
        subprocess.run([gnuplot_exe] + sys.argv[1:], check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        # Gnuplot handles Ctrl-C, so we don't need to do anything here.
        pass


if __name__ == "__main__":
    main()
