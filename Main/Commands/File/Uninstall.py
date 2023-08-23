#!/usr/bin/env python3

import sys
import os

library_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Library"))
sys.path.append(library_dir)

from Modules import find_args
from Modules import subprocess
from Modules import shutil

COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

def uninstall_package_with_pip(package_name):
    try:
        completed_process = subprocess.run(["pip3", "uninstall", "-y", package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        if "WARNING: Skipping" in completed_process.stderr:
            print(f"{COLOR_RED}pip3 uninstallation of {package_name} failed{COLOR_END}")
            return False
        print(f"{COLOR_GREEN}Successfully uninstalled {package_name} using pip3{COLOR_END}")
        return True
    except subprocess.CalledProcessError:
        print(f"{COLOR_RED}pip3 uninstallation of {package_name} failed{COLOR_END}")
        return False

def uninstall_package_with_apt(package_name):
    try:
        subprocess.run(["sudo", "apt", "remove", "-y", package_name], check=True)
        print(f"{COLOR_GREEN}Successfully uninstalled {package_name} using apt{COLOR_END}")
        return True
    except subprocess.CalledProcessError:
        print(f"{COLOR_RED}apt uninstallation of {package_name} failed{COLOR_END}")
        return False

def uninstall_downloaded_package(package_name):
    if os.path.exists(package_name):
        try:
            if os.path.isdir(package_name):
                shutil.rmtree(package_name)
            else:
                os.remove(package_name)
            print(f"{COLOR_GREEN}Successfully removed {package_name}{COLOR_END}")
            return True
        except Exception as e:
            print(f"{COLOR_RED}Failed to remove {package_name}: {e}{COLOR_END}")
            return False

def uninstall_package(package_name):
    if uninstall_package_with_pip(package_name) or uninstall_package_with_apt(package_name) or uninstall_downloaded_package(package_name):
        print(f"{COLOR_GREEN}Package {package_name} successfully uninstalled{COLOR_END}")
    else:
        print(f"{COLOR_RED}Failed to uninstall package {package_name}{COLOR_END}")

def main():
    args = find_args()
    if len(args) >= 1:
        package_name = args[0]
        uninstall_package(package_name)

if __name__ == "__main__":
    main()
