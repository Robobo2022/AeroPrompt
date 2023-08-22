#!/bin/bash

REPO_URL="https://github.com/Robobo2022/AeroPrompt.git"
REPO_DIR="$HOME/AeroPrompt"

if [ -d "$REPO_DIR" ]; then
    echo "Repository directory already exists. Removing existing repository..."
    rm -rf "$REPO_DIR"
fi
git clone "$REPO_URL" "$REPO_DIR"

echo 'export PATH="$HOME/AeroPrompt/Main/Core:$PATH"' >> ~/.bashrc

source ~/.bashrc

chmod +x "$REPO_DIR/Main/Core/Init.py"

ln -s "$REPO_DIR/Main/Core/Init.py" "$REPO_DIR/Main/Core/AeroPrompt"

REQUIREMENTS_FILE="$REPO_DIR/Main/Core/requirements.txt"
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing requirements from $REQUIREMENTS_FILE..."
    if pip3 install -r "$REQUIREMENTS_FILE"; then
        echo 'AeroPrompt is ready to use.'
    else
        echo 'Failed to install requirements.'
    fi
else
    echo "No requirements file found."
fi
