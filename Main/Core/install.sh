#!/bin/bash

# Clone the repository
git clone https://github.com/Robobo2022/Terminal.git ~/custom_scripts/RoboboTerminal

# Make the Init.py script executable
chmod +x ~/custom_scripts/RoboboTerminal/Main/Core/Init.py

# Add the directory containing the script to PATH
echo 'export PATH="$HOME/custom_scripts/RoboboTerminal/Main/Core:$PATH"' >> ~/.bashrc

echo "Installation completed. You can now use the 'Init' terminal command."
