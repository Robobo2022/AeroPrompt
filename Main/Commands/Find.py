#!/usr/bin/env python3

import sys
import os
library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import find_additional_args

def main():
    first_arg = find_additional_args()
    if first_arg:
        print(first_arg)
    else:
        print("No additional args provided")

if __name__ == "__main__":
    main()
