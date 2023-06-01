def charFrequency(string):
    frequencies = {}
    for char in string:
        if char  not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1
    return frequencies

print(charFrequency("i've got the rhythm - the algorithm rythm"))
