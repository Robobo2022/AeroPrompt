#!/usr/bin/env python3

import sys
import os

library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import find_args
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
        print(f"{COLOR_RED}pip3 installation of {package_name} failed, attempting other methods...{COLOR_END}")
        install_package_using_alternatives(package_name)

def install_package_using_alternatives(package_name):
    if try_wget(package_name) or try_curl(package_name) or try_github(package_name):
        print(f"{COLOR_GREEN}Package {package_name} successfully downloaded{COLOR_END}")
    elif subprocess.CalledProcessError:
        print(f"{COLOR_RED}Installation of {package_name} failed{COLOR_END}")

def try_wget(package_name):
    print(f"Trying to download using wget: {COLOR_YELLOW}{package_name}{COLOR_END}")
    try:
        subprocess.run(["wget", package_name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def try_curl(package_name):
    print(f"Trying to download using curl: {COLOR_YELLOW}{package_name}{COLOR_END}")
    try:
        subprocess.run(["curl", "-O", package_name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def try_github(package_name):
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
    args = find_args()
    if len(args) >= 1:
        package_name = args[0]
        install_package_with_pip(package_name)

if __name__ == "__main__":
    main()