#!/usr/bin/env python3

import os
import subprocess
import sys

def find_paths(filename, search_dir):
    found_paths = []
    for root, dirs, files in os.walk(search_dir):
        if filename in files:
            found_paths.append(os.path.join(root, filename))
    return found_paths

def run_path(script_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    commands_dir = os.path.join(base_dir, "..", "Commands")
    
    target_paths = find_paths(script_name, commands_dir)
    for path in target_paths:
        subprocess.run([sys.executable, path] + sys.argv[2:])