#!/usr/bin/env python3

import sys
import os
import requests

library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import find_additional_args

COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

def main():
    additional_args = find_additional_args()
    if len(additional_args) == 1:
        link = additional_args[0]
        
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "http://" + link  # Add http:// prefix if not provided
        
        try:
            response = requests.get(link)
        except requests.exceptions.RequestException:
            print(f"{COLOR_RED}Error: Invalid link{COLOR_END}")
            return 

        print("HTTP Status Code:", response.status_code)
        if response.status_code >= 200 and response.status_code < 300:
            print(f"{COLOR_GREEN}Success!{COLOR_END}")
        elif response.status_code >= 400 and response.status_code < 500:
            print(f"{COLOR_RED}Client Error!{COLOR_END}")
        elif response.status_code >= 500:
            print(f"{COLOR_RED}Server Error!{COLOR_END}")

if __name__ == "__main__":
    main()

        
