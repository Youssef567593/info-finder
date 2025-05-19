#!/bin/bash

echo "[+] Installing Info Finder..."
infofinder
cp info-finder.py $PREFIX/bin/infofinder
chmod +x $PREFIX/bin/infofinder

echo "[+] Installation complete!"
echo "Run the tool using: infofinder"
