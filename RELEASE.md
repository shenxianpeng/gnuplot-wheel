# Release Process

## How to Release a New Gnuplot Version

This project builds gnuplot wheels for specific gnuplot versions. To release a new version:

### 1. Update the version in `pyproject.toml`

Edit `pyproject.toml` and update the version to match the gnuplot version you want to build:

```toml
[project]
version = "6.0.1"  # Change to desired gnuplot version
```

### 2. Create and push a git tag

```bash
# For gnuplot version 6.0.1
git tag v6.0.1
git push origin v6.0.1
```

### 3. Workflow will automatically:

- Extract the version from the tag (e.g., `v6.0.1` → `6.0.1`)
- Clone gnuplot from the corresponding tag (`tags/6.0.1`)
- Build wheels for all platforms
- Publish to PyPI

## Available Gnuplot Tags

See all available gnuplot tags at:
https://sourceforge.net/p/gnuplot/gnuplot-main/ref/master/tags/

## Version Mapping

- Your git tag: `v6.0.1`
- Gnuplot tag: `tags/6.0.1`
- PyPI package version: `6.0.1`
- Windows binary: Downloads from SourceForge for version `6.0.1`

## Manual Testing

To test a specific version locally before releasing:

```bash
# Set the version
export GNUPLOT_VERSION=6.0.1
export GNUPLOT_TAG=tags/6.0.1

# Build
python3 -m build
```
