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

    file_to_zip = sys.argv[1]

    if not os.path.exists(file_to_zip):
        print(f"{COLOR_RED}Error: File '{file_to_zip}' not found.{COLOR_END}")
        sys.exit(1)

    file_base_name = os.path.basename(file_to_zip)
    output_zip_file = os.path.join(os.path.dirname(file_to_zip), f"{file_base_name}.zip")

    try:
        with zipfile.ZipFile(output_zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_to_zip, file_base_name)
        print(f"{COLOR_GREEN}Added {file_to_zip} to {output_zip_file}{COLOR_END}")
    except Exception as e:
        print(f"{COLOR_RED}Error: Could not create zip file: {e}{COLOR_END}")

if __name__ == "__main__":
    main()
