#!/bin/bash

# Download the remote script
wget -O Init.py https://raw.githubusercontent.com/Robobo2022/Terminal/main/Main/Core/Init.py

# Make the downloaded script executable
chmod +x Init.py

# Move the script to a directory in your PATH
mkdir -p ~/custom_scripts
mv Init.py ~/custom_scripts/

# Add the directory to PATH
echo "export PATH=\"$HOME/custom_scripts:\$PATH\"" >> ~/.bashrc
source ~/.bashrc

echo "Installation completed. You can now use the 'Init.py' terminal command."
