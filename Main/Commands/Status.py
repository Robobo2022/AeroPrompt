#!/usr/bin/env python3

import sys
import os
import requests

library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import find_additional_args

def main():
    additional_args = find_additional_args()
    if len(additional_args) >= 1:
        link = additional_args[0]
        try:
            response = requests.get(link)
        except requests.exceptions.RequestException:
            print("\033[31mError: Invalid link\033[0m")
            return 

        print("HTTP Status Code:", response.status_code)
        if response.status_code >= 200 and response.status_code < 300:
            print("\033[32mSuccess!\033[0m")
        elif response.status_code >= 400 and response.status_code < 500:
            print("\033[33mClient Error!\033[0m")
        elif response.status_code >= 500:
            print("\033[31mServer Error!\033[0m")
    else:
        print("Usage: ping <link>")

if __name__ == "__main__":
    main()
