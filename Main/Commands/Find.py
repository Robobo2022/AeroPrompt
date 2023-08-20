#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    
    additional_args = sys.argv[1:]
    if additional_args:
        first_arg = additional_args[0]
        print(f"Prefix script executed with first additional arg: {first_arg}")
    else:
        print("No additional args provided")

if __name__ == "__main__":
    main()
