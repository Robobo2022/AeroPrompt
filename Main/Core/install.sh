#!/bin/bash

REPO_URL="https://github.com/Robobo2022/AeroPrompt.git"

REPO_DIR=~/custom_scripts/RoboboTerminal

if [ -d "$REPO_DIR" ]; then
    echo "Repository directory already exists. Removing existing repository..."
    rm -rf "$REPO_DIR"
fi

git clone "$REPO_URL" "$REPO_DIR"

echo 'export PATH="$HOME/custom_scripts/RoboboTerminal/Main/Core:$PATH"' >> ~/.bashrc

source ~/.bashrc

chmod +x ~/custom_scripts/RoboboTerminal/Main/Core/Init.py

ln -s ~/custom_scripts/RoboboTerminal/Main/Core/Init.py ~/custom_scripts/RoboboTerminal/Main/Core/Init

echo "Installation completed. You can now use the 'Init' terminal command."


