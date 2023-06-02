import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {} #empty dictionary

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save(SAVED_DATA, data)
        print("Data saved")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Invalid command.")
else:
    print("Please enter a single command.")