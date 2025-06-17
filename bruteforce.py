import sys
from collections import Counter

_AN = ((48, 57), (65, 90), (97, 122))
_NAN = ((33, 126),)

def shift(c: int, n: int, set: tuple) -> int:
    if c is None:
        return c
    if c == 32:
        return 32
    for start, end in set:
        if start <= c <= end:
            size = end - start + 1
            return start + (c - start + n) % size
    return c

def decrypt(text: str, n: int, isalphanum: bool) -> str:
    if isalphanum:
        shifted = []
        ascii = [ord(c) if c.isalnum() else 32 if ord(c) == 32 else None for c in text]
        for c in ascii:
            shifted.append(shift(c, -n, _AN))
    else:
        shifted = []
        ascii = [ord(c) if c.isascii() else 32 if ord(c) == 32 else None for c in text]
        for c in ascii:
            shifted.append(shift(c, -n, _NAN))
    return shifted

def brutedecrypt(text: str, isalphanum: bool) -> str:
    tries = []

    if isalphanum:
        for n in range(1, 26):
            decrypted = decrypt(text, n, isalphanum)
            decrypted = ''.join(chr(c) if c != None else "" for c in decrypted)
        
            tries.append([decrypted, "shift: " + str(n)])
    else:
        for n in range(1, 94):
            decrypted = decrypt(text, n, isalphanum)
            decrypted = ''.join(chr(c) if c != None else "" for c in decrypted)

            tries.append([decrypted, "shift: " + str(n)])
    return tries

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Pass arguments in the format of python xxx.py \"Text\" isalphanumeric")
        sys.exit(1)
    
    text = sys.argv[1]

    isalphanum = sys.argv[2].lower()
    if isalphanum == "true":
        isalphanum = True
    elif isalphanum == "false":
        isalphanum = False
    else:
        print("Alphanumeric status must be a boolean")
        sys.exit(1)
    
    tries = brutedecrypt(text, isalphanum)
    
    for Try in tries:
        print(Try[0] + ", " + Try[1])