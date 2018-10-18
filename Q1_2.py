def checkPermutation(stringa, stringb) :
    hsh = {}
    for ch in stringa:
        if ch not in hsh:
            hsh[ch] = 1
        else :
            hsh[ch] += 1
    for ch in stringb :
        if ch not in hsh :
            return False
        hsh[ch] -= 1
        if hsh[ch] < 0 :
            return False
    for k, v in hsh.items() :
        if v != 0 :
            return False
    return True
