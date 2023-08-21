#!/usr/bin/env python3

import sys

def find_args():
    if len(sys.argv) < 2:
        return []
    return [arg.lower() for arg in sys.argv[1:]]
