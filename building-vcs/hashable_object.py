import hashlib

def main():
    file = input("Enter files to use as input: ")
    type = input("Enter one of blob | tree | commit:" )
    with open(file, "rb") as f:
        byte_data = f.read()

    print(hash_object(byte_data, type))



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

    # hashlib.sha1 produces a 160 bit (20 byte) fingerprint which we can extract in the next step
    sha1_hash = hashlib.sha1(header.encode('utf-8') + content) 

    # return the 20 raw bytes into hexadecimal text where each single byte (number between 0-255)
    # gets written out as exactly 2 hex characters (between 0-9 and a-f)
    # 20 bytes * 2 hex characters per byte = 40 character hashed text
    return sha1_hash.hexdigest()

if __name__ == "__main__":
    main()