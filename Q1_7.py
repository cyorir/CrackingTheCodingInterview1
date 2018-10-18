def rotateClockwise90(mat) :
    from math import floor, ceil
    m = len(mat)-1
    for i in range(floor(len(mat)/2)) :
        for j in range(ceil(len(mat)/2)) :
            tmp = mat[i][j]
            mat[i][j] = mat[m-j][i]
            mat[m-j][i] = mat[m-i][m-j]
            mat[m-i][m-j] = mat[j][m-i]
            mat[j][m-i] = tmp
    return mat
