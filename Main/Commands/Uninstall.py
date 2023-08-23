#!/usr/bin/env python3

import sys
import os

library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import find_args
from Library.Modules import subprocess
from Library.Modules import shutil

COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

def uninstall_package_with_pip(package_name):
    try:
        subprocess.run(["pip3", "uninstall", "-y", package_name], check=True)
        print(f"{COLOR_GREEN}Successfully uninstalled {package_name} using pip3{COLOR_END}")
    except subprocess.CalledProcessError:
        print(f"{COLOR_RED}pip3 uninstallation of {package_name} failed{COLOR_END}")

def uninstall_downloaded_package(package_name):
    if os.path.exists(package_name):
        try:
            if os.path.isdir(package_name):
                shutil.rmtree(package_name)
            else:
                os.remove(package_name)
            print(f"{COLOR_GREEN}Successfully removed {package_name}{COLOR_END}")
        except Exception as e:
            print(f"{COLOR_RED}Failed to remove {package_name}: {e}{COLOR_END}")

def uninstall_package(package_name):
    uninstall_package_with_pip(package_name)
    uninstall_downloaded_package(package_name)

def main():
    args = find_args()
    if len(args) >= 1:
        package_name = args[0]
        uninstall_package(package_name)

if __name__ == "__main__":
    main()
