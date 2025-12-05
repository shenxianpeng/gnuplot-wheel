#!/bin/bash
# Setup build dependencies for Linux
# This script handles both apt-get (Debian/Ubuntu) and yum (RHEL/CentOS) package managers
set -e

echo "Installing build dependencies for Linux..."

if command -v yum >/dev/null 2>&1; then
  echo "Detected yum package manager (RHEL/CentOS)"
  yum install -y readline-devel libpng-devel zlib-devel libjpeg-devel wget freetype-devel fontconfig-devel
  
  # Build libgd from source with FreeType support (system version is too old in RHEL/CentOS)
  echo "Building libgd from source..."
  cd /tmp
  wget https://github.com/libgd/libgd/releases/download/gd-2.3.3/libgd-2.3.3.tar.gz
  tar -xzf libgd-2.3.3.tar.gz
  cd libgd-2.3.3
  ./configure --prefix=/usr/local --with-freetype
  make -j$(nproc)
  make install
  ldconfig
  echo "libgd built and installed successfully"
  
elif command -v apt-get >/dev/null 2>&1; then
  echo "Detected apt-get package manager (Debian/Ubuntu)"
  apt-get update
  apt-get install -y libgd-dev libreadline-dev libpng-dev zlib1g-dev libjpeg-dev libfreetype6-dev libfontconfig1-dev
  
else
  echo "ERROR: No supported package manager found (yum or apt-get)!" >&2
  exit 1
fi

echo "Linux build dependencies installed successfully"
