#!/usr/bin/env python3

import sys
import os
library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import run_path

def main():
    if len(sys.argv) < 2:
        print("Usage: AeroPrompt <command> [args]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "find":
        run_path("Find.py")
    elif command == "help":
        print("Commands:")
        print("Find <search_query> <num_links>")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
