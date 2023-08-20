#!/bin/bash

git clone https://github.com/Robobo2022/Terminal.git ~/custom_scripts/RoboboTerminal

chmod +x ~/custom_scripts/RoboboTerminal/Main/Core/Init.py

echo 'export PATH="$HOME/custom_scripts/RoboboTerminal/Main/Core:$PATH"' >> ~/.bashrc

echo "Installation completed. You can now use the 'Init' terminal command."
