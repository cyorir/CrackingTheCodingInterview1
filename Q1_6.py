def stringCompression(a) :
    i = 0
    chcount = 0
    ret = ""
    prevch = ""
    while i < len(a) :
        if a[i] != prevch and prevch != "":
            ret += prevch + str(chcount)
            chcount = 0
        chcount += 1
        prevch = a[i]
        i += 1
    if chcount != 0 :
        ret += prevch + str(chcount)
    if len(ret) < len(a) :
        return ret
    return a
