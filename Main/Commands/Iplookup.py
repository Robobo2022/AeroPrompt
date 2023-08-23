#!/usr/bin/env python3

import sys
import os
library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.Modules import find_args
from Library.Modules import socket
from Library.Modules import requests

def lookup_ip_info(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        host_name_info = f"{host_name[0]} ({host_name[2][0]})"
    except socket.herror:
        host_name_info = "Not Found"
    
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        
        ip_info = {
            "IP Address": ip_address,
            "Host Name": host_name_info,
            "Location": data.get("city", "Unknown City"),
            "Region": data.get("region", "Unknown Region"),
            "Country": data.get("country", "Unknown Country"),
            "Organization": data.get("org", "Unknown Organization"),
            "Timezone": data.get("timezone", "Unknown Timezone"),
            "Coordinates": data.get("loc", "Unknown Coordinates")
        }
        
        return "\n".join([f"{key}: {value}" for key, value in ip_info.items()])
    except Exception as e:
        return f"IP Address: {ip_address}\nError: {e}"

def main():
    args = find_args()
    if len(args) == 1:
        ip_address = args[0]
        info = lookup_ip_info(ip_address)
        print(info)
    else:
        print("Usage: iplookip <ip_address>")

if __name__ == "__main__":
    main()
