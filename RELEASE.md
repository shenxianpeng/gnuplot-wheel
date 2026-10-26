# Release Process

## How to Release a New Gnuplot Version

This project builds gnuplot wheels for specific gnuplot versions. The package
version comes from the git tag (via `setuptools_scm`), so there is nothing to
edit in `pyproject.toml`.

### 1. Check the upstream release

Before tagging, make sure gnuplot has published everything the build needs:

- The source tag exists (used by the Linux and macOS builds):

  ```bash
  git ls-remote --tags https://git.code.sf.net/p/gnuplot/gnuplot-main | grep 6.0.1
  ```

- A Windows binary exists in
  `https://sourceforge.net/projects/gnuplot/files/gnuplot/6.0.1/`.
  The build looks for these files, in order:
  `gpXXX-win64-mingw.zip`, `gpXXX-win64-mingw.exe`, `gpXXX-win64-clang.exe`.
  If upstream renames the file again, update `gnuplot_wheel/build.py` first.

### 2. Dry-run the build (optional, recommended)

Run the `main` workflow manually with the new version. This builds wheels for
all platforms without publishing to PyPI:

```bash
gh workflow run main.yml -f gnuplot_version=6.0.1 -f publish_testpypi=false
```

### 3. Create and push a git tag

```bash
# For gnuplot version 6.0.1
git tag v6.0.1
git push origin v6.0.1
```

### 4. Workflow will automatically:

- Extract the version from the tag (e.g., `v6.0.1` → `6.0.1`)
- Clone gnuplot from the corresponding tag (`6.0.1`)
- Build wheels for all platforms
- Publish to PyPI

Then publish the GitHub release that Release Drafter has prepared for the tag.

## Available Gnuplot Tags

See all available gnuplot tags at:
https://sourceforge.net/p/gnuplot/gnuplot-main/ref/master/tags/

## Version Mapping

- Your git tag: `v6.0.1`
- Gnuplot tag: `6.0.1`
- PyPI package version: `6.0.1`
- Windows binary: Downloads from SourceForge for version `6.0.1`

## Manual Testing

To test a specific version locally before releasing:

```bash
# Set the version
export GNUPLOT_VERSION=6.0.1
export GNUPLOT_TAG=6.0.1

# Build
python3 -m build
```
