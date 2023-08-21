#!/usr/bin/env python3

import os
import subprocess
import sys

def find_path(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, filename)

def run_path(Path):
    prefix_script_path = find_path(os.path.join("..", "Commands", Path))
    subprocess.run([sys.executable, prefix_script_path] + sys.argv[2:])
