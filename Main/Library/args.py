#!/usr/bin/env python3

import sys

def find_additional_args():
    if len(sys.argv) < 2:
        sys.exit(1)

    additional_args = sys.argv[1:]
    return tuple(additional_args)

if __name__ == "__main__":
    additional_args = find_additional_args()

    if additional_args:
        first_arg = additional_args[0]
        second_arg = additional_args[1] if len(additional_args) > 1 else None
        third_arg = additional_args[2] if len(additional_args) > 2 else None
    else:
        print("No additional args provided")
