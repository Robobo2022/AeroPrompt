#!/usr/bin/env python3

import sys
import os
library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import find_additional_args
from Library.Modules import requests
from Library.Modules import BeautifulSoup
from Library.Modules import json

COLOR_GREEN = "\033[92m"
COLOR_END = "\033[0m"

def main():
    additional_args = find_additional_args()
    if len(additional_args) >= 2:
        first_arg = additional_args[0]
        num_links = int(additional_args[1])
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
