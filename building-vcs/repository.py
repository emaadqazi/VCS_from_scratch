import os 
import json
from objects import hash_object, write_object, read_object

def main():
    testFile = input("What file do you want to add? ")
    add(testFile)


def init():
    """
    Initializes .pygit/objects and .pygit /refs/heads and .pygit/HEAD in root directory if DNE
    """
    # makedirs is going to create the folder if it DNE, but not if it does exist avoiding error trapping completely
    os.makedirs(".pygit", exist_ok=True)
    os.makedirs(".pygit/objects", exist_ok=True)
    os.makedirs(".pygit/refs/heads", exist_ok=True)

    # initializing HEAD
    filepath = ".pygit/HEAD"
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write("ref: refs/heads/main")
    else:
        print("HEAD already exists!")

def add(fileToAdd):

    # Reading the files contents
    try:
        with open(fileToAdd, "rb") as file:
            data = file.read()
    except FileNotFoundError:
        print("File does not exist")
        return 

    # Store the file as a blob
    stored = write_object(data, "blob")

    # Read existing index if it exists 
    try:
        with open(".pygit/index", "r") as file: # writing will kill the contents, need to read first
            index = json.load(file)
    except FileNotFoundError: # JSON does not exist, need to initialize
        print("Index does not exist. Initializing...")
        index = {}

    except json.JSONDecodeError:
        print("Error: The file exists, but contains invalid JSON.")
        return

    # Add/update the file in the index
    index[fileToAdd] = stored # stores { fileName : hash value }

    # Write updated index back to disk. Writing will automatically create if it does not exist
    with open(".pygit/index", "w") as file:
        json.dump(index, file, indent=4)

if __name__ == "__main__":
    main()