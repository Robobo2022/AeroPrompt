#!/bin/bash

wget -O Init https://raw.githubusercontent.com/Robobo2022/Terminal/main/Main/Core/Init.py

chmod +x Init

mkdir -p ~/custom_scripts
mv Init ~/custom_scripts/

# Add the directory to PATH
echo 'export PATH="$HOME/custom_scripts:$PATH"' >> ~/.bashrc
source ~/.bashrc

echo "Installation completed. You can now use the 'Init' terminal command."
