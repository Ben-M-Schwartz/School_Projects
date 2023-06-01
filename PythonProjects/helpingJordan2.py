def vigenere(string, key):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = string.upper()
    key = key.upper()
    klen = len(key)

    newString = ""

    n=0
    for char in string:
        pos = LETTERS.index(char)
        print(pos)
        kchar = key[n%klen]
        print(kchar)
        shift = LETTERS.index(kchar)
        print(shift)
        n = n+1

        newPos = (pos+shift)%26
        print(newPos)

        newChar = LETTERS[newPos]
        print(newChar)

        newString = newString + newChar

    return newString

print(vigenere("t", "p"))

    
        
