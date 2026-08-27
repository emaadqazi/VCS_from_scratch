import hashlib
import os 
import zlib 

def main():
    # file = input("Enter files to use as input: ")
    file = "test.txt"
    type = input("Enter one of blob | tree | commit: ")
    with open(file, "rb") as f:
        byte_data = f.read()

    # print(hash_object(byte_data, type))
    print(write_object(byte_data, type))



def hash_object(content, type) -> str:
    """
    Computes the Git-style SHA-1 hash of content, prefixed with a header

    Args:
        content: the real data, as bytes (reading from a file)
        type: a label, one of "blob" | "tree" | commit. Tells the function what type of object this is

    Returns:
        hash: 40-char hex digest using SHA-1
    """

    # the header is essentially a "label taped onto a box before we seal it shut"
    # header specifies type (blob | tree | commit)
    # if a blob and tree contained the same amount of raw bytes, without labelling it,
    # could not tell them apart.
    # we are going to use this later for lookups 
    header = f"{type} {len(content)}\0"
    print(header)

    # hashlib.sha1 produces a 160 bit (20 byte) fingerprint which we can extract in the next step
    sha1_hash = hashlib.sha1(header.encode('utf-8') + content) 

    # return the 20 raw bytes into hexadecimal text where each single byte (number between 0-255)
    # gets written out as exactly 2 hex characters (between 0-9 and a-f)
    # 20 bytes * 2 hex characters per byte = 40 character hashed text
    return sha1_hash.hexdigest()

def write_object(content, type):

    # need to refactor this function later so that we are not repeating ourself 
    # or we will use the hash_object() function from main and send that value down here when we write
    header = f"{type} {len(content)}\0"
    sha1_hash = (hashlib.sha1(header.encode('utf-8') + content).hexdigest())
    print(sha1_hash)

    # slice the first 2 indices to use as a folder path
    # so that we end up with something like:
    # .pygit/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391
    subfolder = sha1_hash[:2] # for better organization
    filename = sha1_hash[2:] # the new file name

    # for compressing the file
    data = header.encode("utf-8") + content
    compressed = zlib.compress(data)

    # metadata = data about data; information describing/organizing data
    # for this, we need to track commits|tree/blob objects, that is not data, rather information about the data we want to capture
    # we are going to store all of this under .pygit instead of .git because then it will mess with actual git
    # .pygit is what allows the history and ability to track changes
    path = f".pygit/objects/{subfolder}" 
    os.makedirs(path, exist_ok=True) # creates the path if it DNE | otherwise leaves it as is
    file_path = os.path.join(path, filename)
    if not os.path.exists(f".pygit/objects/{subfolder}/{filename}"):
        print("Nothing exists here!")
        with open(file_path, "wb") as file:
                        file.write(compressed)
    else:
          print("The same hash exists here.")
                    

    return sha1_hash

if __name__ == "__main__":
    main()