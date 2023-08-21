import os
import json
import sys

json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Commands.json')
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

def main():
    if len(sys.argv) == 2:
        title = sys.argv[1]

        if title in data:
            script_filename = data[title]["File"]
            script_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts", script_filename))
            
            if os.path.exists(script_path):
                exec(open(script_path).read())
            else:
                print(f"Script file '{script_filename}' not found.")
        else:
            print(f"No data found for '{title}'")
    else:
        print("Usage: python script.py [title]")

if __name__ == "__main__":
    main()
