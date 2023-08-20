#!/bin/bash

# Make the script executable
chmod +x mycommand.py

# Add script directory to PATH
SCRIPT_DIR="$(pwd)"
echo "export PATH=\"$SCRIPT_DIR:\$PATH\"" >> ~/.bashrc

# Reload the shell configuration
source ~/.bashrc

echo "Installation completed. You can now use the 'mycommand' terminal command."
