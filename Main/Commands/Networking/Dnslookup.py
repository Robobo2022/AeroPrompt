#!/usr/bin/env python3

import sys
import os

library_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Library"))
sys.path.append(library_dir)

from Modules import find_args
from Modules import socket
from Modules import requests

COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def dns_lookup(domain):
    try:
        ip_addresses = socket.getaddrinfo(domain, None)
        print(f"IP addresses for {COLOR_GREEN}{domain}{COLOR_END}:")
        for result in ip_addresses:
            ip_address = result[4][0]
            try:
                host_name, _, _ = socket.gethostbyaddr(ip_address)
            except socket.herror:
                host_name = "N/A"
            
            ip_info = get_ip_info(ip_address)
            if ip_info:
                print(f"{COLOR_YELLOW}IP: {ip_address} | Hostname: {host_name}{COLOR_END}")
                print(f"{COLOR_YELLOW}Location: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}{COLOR_END}")
                print(f"{COLOR_YELLOW}Organization: {ip_info.get('org', 'N/A')}{COLOR_END}")
                print("-" * 50)
            else:
                print(f"{COLOR_YELLOW}IP: {ip_address} | Hostname: {host_name} | Unable to retrieve additional info{COLOR_END}")
                print("-" * 50)
    except socket.gaierror as e:
        print(f"{COLOR_RED}Error: {e}{COLOR_END}")

if __name__ == "__main__":
    args = find_args()
    if len(args) == 1:
        domain_name = args[0]
        dns_lookup(domain_name)