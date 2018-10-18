def rotateString(a) :
    return a[-1] + a[:len(a)-1]

def isRotation(a, b) :
    if a == b :
        return True
    c = rotateString(a)
    while c != a :
        if c == b :
            return True
        c = rotateString(c)
    return False
