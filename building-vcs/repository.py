import os 
from objects import hash_object, write_object, read_object

def main():
    init()

def init():

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

if __name__ == "__main__":
    main()