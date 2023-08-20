#!/bin/bash

# Download the remote script
wget -O Init.py https://raw.githubusercontent.com/Robobo2022/Terminal/main/Main/Core/Init.py

chmod +x Init.py

mkdir -p ~/custom_scripts
mv Init.py ~/custom_scripts/

# Add the directory to PATH
echo "export PATH=\"$HOME/custom_scripts:\$PATH\"" >> ~/.bashrc
source ~/.bashrc

echo "Installation completed. You can now use the 'Init.py' terminal command."
