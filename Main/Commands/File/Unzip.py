#!/usr/bin/env python3

import sys
import os
library_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Library"))
sys.path.append(library_dir)
from Modules import zipfile

COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    zip_file_to_extract = sys.argv[1]

    if not os.path.exists(zip_file_to_extract):
        print(f"{COLOR_RED}Error: Zip file '{zip_file_to_extract}' not found.{COLOR_END}")
        sys.exit(1)

    try:
        with zipfile.ZipFile(zip_file_to_extract, "r") as zipf:
            extract_dir = os.path.dirname(zip_file_to_extract)
            zipf.extractall(extract_dir)
        print(f"{COLOR_GREEN}Extracted {zip_file_to_extract} to {extract_dir}{COLOR_END}")
    except Exception as e:
        print(f"{COLOR_RED}Error: Could not extract zip file: {e}{COLOR_END}")

if __name__ == "__main__":
    main()
