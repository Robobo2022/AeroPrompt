import subprocess
import sys
import os
library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(library_parent_dir)

from Library.find_path import find_path

def main():
    if len(sys.argv) < 2:
        print("Usage: Init <command> [args]")
        sys.exit(1)
    command = sys.argv[1]

    if command == "Find":
        prefix_script_path = find_path(os.path.join("..", "Commands", "Find.py"))
        subprocess.run([sys.executable, prefix_script_path] + sys.argv[2:])
    elif command == "Help":
        print("Help")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
