#!/usr/bin/env python3

import subprocess

def main():
    new_prefix = "noob"
    subprocess.run(["python3", "change_prefix.py", "Init.py", new_prefix])

    # Now, you can execute your main functionality
    print("Sippington city shall we")

if __name__ == "__main__":
    main()
