#!/usr/bin/env python3

import sys
import os

library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import find_additional_args
from Library.Modules import subprocess
from Library.Modules import requests
from Library.Modules import BeautifulSoup
from Library.Modules import json

COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

def install_package_with_pip(package_name):
    try:
        subprocess.run(["pip3", "install", package_name], check=True)
        print(f"{COLOR_GREEN}Successfully installed {package_name} using pip3{COLOR_END}")
    except subprocess.CalledProcessError:
        print(f"{COLOR_RED}pip3 installation of {package_name} failed, attempting to clone from Git...{COLOR_END}")
        install_package_with_git(package_name)

def install_package_with_git(package_name):
    github = requests.get(f"https://github.com/search?q={package_name}&type=repositories")
    soup = BeautifulSoup(github.text, "html.parser")
    json_data = soup.text[soup.text.find('{'):]
    data = json.loads(json_data)
    results = data.get("payload", {}).get("results", [])
    if results:
        name = results[0].get("hl_name", "")
        repo_link = f"https://github.com/{name}.git"
        print(f"Cloning {COLOR_YELLOW}{repo_link}{COLOR_END}...")
        subprocess.run(["git", "clone", repo_link])
        print(f"{COLOR_GREEN}Successfully cloned {repo_link}{COLOR_END}")
    else:
        print(f"{COLOR_RED}No Git repository found for {package_name}{COLOR_END}")

def main():
    additional_args = find_additional_args()
    if len(additional_args) >= 1:
        package_name = additional_args[0]
        install_package_with_pip(package_name)
    else:
        print(f"Usage: {COLOR_GREEN}Install {COLOR_YELLOW}<package_name>{COLOR_END}")

if __name__ == "__main__":
    main()
