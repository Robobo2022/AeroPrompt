#!/usr/bin/env python3

import sys
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
library_parent_dir = os.path.abspath(os.path.join(script_directory, ".."))
sys.path.append(library_parent_dir)

from Library.Modules import run_subprocess_for_find

def main():
    if len(sys.argv) < 2:
        print("Usage: Init <command> [args]")
        sys.exit(1)
    command = sys.argv[1]

    if command == "Find":
        run_subprocess_for_find()
    elif command == "Help":
        print("Help")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
