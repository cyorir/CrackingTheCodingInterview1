def editDistance(a,b) :
    opt = []
    for i in range(len(a)+1) :
        opt.append([])
        for j in range(len(b)+1) :
            opt[i].append(0)
    for i in range(1,len(a)+1) :
        for j in range(1,len(b)+1) :
            if a[i-1] == b[j-1] :
                opt[i][j] = opt[i-1][j-1]
            else :
                opt[i][j] = min(1+opt[i-1][j],1+opt[i][j-1],1+opt[i-1][j-1])
    return opt[-1][-1]

def editSingle(a, b) :
    return editDistance(a,b) <= 1
