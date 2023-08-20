import sys
import os
library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
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
