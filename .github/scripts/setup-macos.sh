#!/bin/bash
# Setup build dependencies for macOS
set -e

echo "Installing build dependencies for macOS..."
brew install autoconf automake libtool gd jpeg git
echo "macOS build dependencies installed successfully"
