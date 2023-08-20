#!/usr/bin/env python3

import os
import sys

def change_prefix(script_path, new_prefix):
    with open(script_path, 'r') as f:
        content = f.read()

    modified_content = content.replace('Init', new_prefix)

    with open(script_path, 'w') as f:
        f.write(modified_content)

def main():
    if len(sys.argv) != 3:
        print("Usage: python change_prefix.py <script_path> <new_prefix>")
        sys.exit(1)

    script_path = os.path.expanduser(sys.argv[1])
    new_prefix = sys.argv[2]

    change_prefix(script_path, new_prefix)
    print(f"Prefix in {script_path} changed to '{new_prefix}'.")

if __name__ == "__main__":
    main()
