def isUnique(string) :
    hsh = {}
    for ch in string :
        if ch in hsh :
            return False
        hsh[ch] = 1
    return True
