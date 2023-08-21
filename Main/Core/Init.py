#!/usr/bin/env python3

import sys
import os
library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import run_path
from Library.Modules import find_args

COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_END = "\033[0m"

def main():
    args = find_args()
    if len(args) < 1:
        print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}<command>{COLOR_END} {COLOR_YELLOW}[args]{COLOR_END}")
        sys.exit(1)

    command = args[0]

    if command == "find":
        if len(args) < 4:
            print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Find {COLOR_YELLOW}<search_query> <num_links>{COLOR_END}")
        else:
            run_path("Find.py")
    elif command == "install":
        if len(args) < 3:
            print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Install {COLOR_YELLOW}<package_name>{COLOR_END}")
        else:
            run_path("Install.py")
    elif command == "status":
        if len(args) < 3:
            print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Status {COLOR_YELLOW}<link>{COLOR_END}")
        else:
            run_path("Status.py")
    elif command == "uname":
        run_path("Uname.py")
    elif command == "help":
        print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} <command> [args]")
        print(f"{COLOR_GREEN}Commands:{COLOR_END}")
        print(f"  {COLOR_YELLOW}find <search_query> <num_links>{COLOR_END}")
        print(f"      {COLOR_BLUE}Search for links based on a query.{COLOR_END}")
        print(f"  {COLOR_YELLOW}install <package_name>{COLOR_END}")
        print(f"      {COLOR_BLUE}Install a package.{COLOR_END}")
        print(f"  {COLOR_YELLOW}Status <link>{COLOR_END}")
        print(f"      {COLOR_BLUE}Checks Status of given link.{COLOR_END}")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
