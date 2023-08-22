#!/usr/bin/env python3

import sys
import os

library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import run_path
from Library.Modules import find_args
from Library.Modules import json

COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

Custom_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Custom")
json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Custom", "Commands.json")

def main():
    args = find_args()
    if len(args) < 1:
        print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}<command>{COLOR_END} {COLOR_YELLOW}[args]{COLOR_END}")
        sys.exit(1)
    command = args[0]

    if command == "find":
        if len(args) < 3:
            print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Find {COLOR_YELLOW}<search_query> <num_links>{COLOR_END}")
        else:
            run_path("Find.py")
    elif command == "install":
        if len(args) < 2:
            print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Install {COLOR_YELLOW}<package_name>{COLOR_END}")
        else:
            run_path("Install.py")
    elif command == "status":
        if len(args) < 2:
            print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Status {COLOR_YELLOW}<link>{COLOR_END}")
        else:
            run_path("Status.py")
    elif command == "uname":
        run_path("Uname.py")
    elif command == "zip":
        if len(args) < 2:
            print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Zip {COLOR_YELLOW}<zip_file>{COLOR_END}")
        else:
            run_path("File/Zip.py")
    elif command == "unzip":
        if len(args) < 2:
            print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Unzip {COLOR_YELLOW}<zip_file>{COLOR_END}")
        else:
            run_path("File/Unzip.py")
    elif command == "iplookup":
        if len(args) < 2:
            print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Iplookup {COLOR_YELLOW}<ip_address>{COLOR_END}")
        else:
            run_path("Iplookup.py")
    elif command == "custom":
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            for title, command_info in data.items():
                usage = command_info["Usage"]
                description = command_info["Description"]
                print(f"{COLOR_YELLOW}{title}{COLOR_END}")
                print(f"  {COLOR_BLUE}{usage}{COLOR_END}")
                print(f"      {COLOR_BLUE}{description}{COLOR_END}")
    elif command == "help":
        print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} <command> [args]")
        print(f"{COLOR_GREEN}Commands:{COLOR_END}")
        print(f"  {COLOR_YELLOW}find <search_query> <num_links>{COLOR_END}")
        print(f"      {COLOR_BLUE}Search for Github repository's based on a query.{COLOR_END}")
        print(f"  {COLOR_YELLOW}install <package_name>{COLOR_END}")
        print(f"      {COLOR_BLUE}Install a package.{COLOR_END}")
        print(f"  {COLOR_YELLOW}Status <link>{COLOR_END}")
        print(f"      {COLOR_BLUE}Check the status of a link.{COLOR_END}")
        print(f"  {COLOR_YELLOW}uname{COLOR_END}")
        print(f"      {COLOR_BLUE}Prints system information.{COLOR_END}")
        print(f"  {COLOR_YELLOW}zip <zip_file>{COLOR_END}")
        print(f"      {COLOR_BLUE}Zip a file.{COLOR_END}")
        print(f"  {COLOR_YELLOW}unzip <zip_file>{COLOR_END}")
        print(f"      {COLOR_BLUE}Unzip a file.{COLOR_END}")
        print(f"  {COLOR_YELLOW}iplookup <ip_address>{COLOR_END}")
        print(f"      {COLOR_BLUE}Lookup information about an IP address.{COLOR_END}")
        print(f"  {COLOR_YELLOW}custom{COLOR_END}")
        print(f"      {COLOR_BLUE}List custom commands.{COLOR_END}")
    else:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            lowercase_command = command.lower()
            for title, command_info in data.items():
                lowercase_title = title.lower()
                if lowercase_command == lowercase_title:
                    run_path(Custom_path + "/" + "scripts/" + command_info["File"])
                    break
            else:
                print(f"{COLOR_RED}Command '{command}' not found. {COLOR_END}")


if __name__ == "__main__":
    main()
