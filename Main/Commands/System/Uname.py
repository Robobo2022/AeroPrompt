#!/usr/bin/env python3

import os
import platform
import socket

def get_system_info():
    info = {}
    info["User"] = os.getlogin()
    info["Hostname"] = platform.node()
    info["OS"] = platform.system()
    info["Kernel Version"] = platform.release()
    info["Architecture"] = platform.machine()
    info["Processor"] = platform.processor()
    info["Home Directory"] = os.path.expanduser("~")
    info["Current Directory"] = os.getcwd()
    info["IP Address"] = socket.gethostbyname(socket.gethostname())

    return info

def main():
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
