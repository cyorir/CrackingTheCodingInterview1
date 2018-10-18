def palindrome_permutation(string):
    hsh = {}
    numOdd = 0
    for ch in string:
        if ch not in hsh :
            hsh[ch] = 0
        hsh[ch] += 1
        if hsh[ch] % 2 == 1 :
            numOdd += 1
        else :
            numOdd -= 1
    if numOdd > 1 :
        return False
    return True
