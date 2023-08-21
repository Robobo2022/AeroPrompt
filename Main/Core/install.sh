#!/bin/bash

REPO_URL="https://github.com/Robobo2022/AeroPrompt.git"
REPO_DIR=~/AeroPrompt

if [ -d "$REPO_DIR" ]; then
    echo "Repository directory already exists. Removing existing repository..."
    rm -rf "$REPO_DIR"
fi

git clone "$REPO_URL" "$REPO_DIR"

echo 'export PATH="$HOME/AeroPrompt/Main/Core:$PATH"' >> ~/.bashrc

source ~/.bashrc

chmod +x ~/AeroPrompt/Main/Core/Init.py

ln -s ~/AeroPrompt/Main/Core/Init.py ~/AeroPrompt/Main/Core/Init

REQUIREMENTS_FILE="$REPO_DIR/Main/Core/requirements.txt"
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing requirements from $REQUIREMENTS_FILE..."
    pip3 install -r "$REQUIREMENTS_FILE"
fi

echo 'AeroPrompt is ready to use.'