def zeroMatrix(mat) :
    zeroCols = []
    zeroRows = []
    for i in range(len(mat)) :
        for j in range(len(mat[i])) :
            if mat[i][j] == 0 :
                if i not in zeroCols :
                    zeroCols.append(j)
                if j not in zeroRows :
                    zeroRows.append(i)
    for col in zeroCols :
        for i in range(len(mat)) :
            mat[i][col] = 0
    for row in zeroRows :
        for j in range(len(mat[row])) :
            mat[row][j] = 0
    return mat
