#!/bin/bash
# Setup build dependencies for Linux
# This script handles both apt-get (Debian/Ubuntu) and yum (RHEL/CentOS) package managers
set -e

# Version of libgd to build from source for RHEL/CentOS
LIBGD_VERSION="2.3.3"

echo "Installing build dependencies for Linux..."

if command -v yum >/dev/null 2>&1; then
  echo "Detected yum package manager (RHEL/CentOS)"
  yum install -y git readline-devel libpng-devel zlib-devel libjpeg-devel wget freetype-devel fontconfig-devel
  
  # Build libgd from source with FreeType support (system version is too old in RHEL/CentOS)
  echo "Building libgd ${LIBGD_VERSION} from source..."
  cd /tmp
  wget "https://github.com/libgd/libgd/releases/download/gd-${LIBGD_VERSION}/libgd-${LIBGD_VERSION}.tar.gz"
  tar -xzf "libgd-${LIBGD_VERSION}.tar.gz"
  cd "libgd-${LIBGD_VERSION}"
  ./configure --prefix=/usr/local --with-freetype
  make -j$(nproc)
  make install
  ldconfig
  echo "libgd built and installed successfully"
  
elif command -v apt-get >/dev/null 2>&1; then
  echo "Detected apt-get package manager (Debian/Ubuntu)"
  apt-get update
  apt-get install -y git libgd-dev libreadline-dev libpng-dev zlib1g-dev libjpeg-dev libfreetype6-dev libfontconfig1-dev
  
else
  echo "ERROR: No supported package manager found (yum or apt-get)!" >&2
  exit 1
fi

echo "Linux build dependencies installed successfully"
