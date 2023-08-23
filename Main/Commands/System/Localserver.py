#!/usr/bin/env python3

import sys
import os
import http.server

library_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Library"))
sys.path.append(library_dir)

COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

from Modules import find_args
from Modules import socketserver
from Modules import webbrowser
from Modules import subprocess
from Modules import run_path

args = find_args()
if len(args) >= 1:
    print(f"Usage: {COLOR_BLUE}AeroPrompt{COLOR_END} {COLOR_GREEN}Localserver {COLOR_YELLOW}<folder_name>{COLOR_END} {COLOR_YELLOW}<ip_address>{COLOR_END} {COLOR_YELLOW}<port>{COLOR_END}")

ip = args[1]
port = int(args[2])
foldername = args[0]

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=foldername, **kwargs)

if not os.path.exists(foldername):
    os.mkdir(foldername)

index_html_content = """
<html>
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <h1>Welcome to my local website!</h1>
    <p>This is a sample paragraph.</p>
</body>
</html>
"""

with open(os.path.join(foldername, "index.html"), "w") as index_file:
    index_file.write(index_html_content)

styles_css_content = """
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

h1 {
    color: #333;
}

p {
    color: #666;
}
"""

with open(os.path.join(foldername, "styles.css"), "w") as css_file:
    css_file.write(styles_css_content)

with socketserver.TCPServer((ip, port), CustomHandler) as server:
    print(f"Server started at {COLOR_GREEN}http://{ip}:{port}{COLOR_END}")

    webbrowser.open(f"http://{ip}:{port}")

    os.system(f"start {os.path.abspath(foldername)}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

