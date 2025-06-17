import sys

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

def encrypt(text: str, n: int, isalphanum: bool) -> str:
    if isalphanum:
        shifted = []
        ascii = [ord(c) if c.isalnum() else 32 if ord(c) == 32 else None for c in text]
        for c in ascii:
            shifted.append(shift(c, n, _AN))
    else:
        shifted = []
        ascii = [ord(c) if c.isascii() else 32 if ord(c) == 32 else None for c in text]
        for c in ascii:
            shifted.append(shift(c, n, _NAN))
    return shifted

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Pass arguments in the format of python xxx.py \"Text\" shift isalphanumeric")
        sys.exit(1)
    
    text = sys.argv[1]

    try:
        n = int(sys.argv[2])
    except ValueError:
        print("Shift must be an integer")
        sys.exit(1)
    
    isalphanum = sys.argv[3].lower()
    if isalphanum == "true":
        isalphanum = True
    elif isalphanum == "false":
        isalphanum = False
    else:
        print("Alphanumeric status must be a boolean")
        sys.exit(1)
    
    result = encrypt(text, n, isalphanum)
    print(''.join(chr(c) if c != None else "" for c in result))