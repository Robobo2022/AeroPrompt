#!/usr/bin/env python3

import sys
import os

library_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Library"))
sys.path.append(library_dir)

from Modules import find_args
from Modules import requests
from Modules import BeautifulSoup
from Modules import json

COLOR_GREEN = "\033[92m"
COLOR_END = "\033[0m"

def main():
    args = find_args()
    if len(args) >= 2:
        first_arg = args[0]
        num_links = int(args[1])
        github = requests.get(f"https://github.com/search?q={first_arg}&type=repositories")
        soup = BeautifulSoup(github.text, "html.parser")
        json_data = soup.text[soup.text.find('{'):]
        data = json.loads(json_data)
        results = data.get("payload", {}).get("results", [])
        
        for i, result in enumerate(results):
            if i >= num_links:
                break
            name = result.get("hl_name", "")
            repo_link = f"{COLOR_GREEN}https://github.com/{name}{COLOR_END}"
            print(repo_link)

if __name__ == "__main__":
    main()
