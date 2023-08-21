#!/usr/bin/env python3

import sys
import os
library_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Library"))
sys.path.append(library_dir)
from Modules import zipfile

COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_END = "\033[0m"

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Zip {COLOR_YELLOW}<zip_file>{COLOR_END}")

    file_to_zip = sys.argv[1]

    if not os.path.exists(file_to_zip):
        print(f"Error: File '{file_to_zip}' not found.")
        sys.exit(1)

    file_base_name = os.path.basename(file_to_zip)
    output_zip_file = os.path.join(os.path.dirname(file_to_zip), f"{file_base_name}.zip")

    with zipfile.ZipFile(output_zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_to_zip, file_base_name)
        print(f"Added {file_to_zip} to {output_zip_file}")

if __name__ == "__main__":
    main()
