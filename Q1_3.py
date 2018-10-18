def URLify(string) :
    i = len(string)-1
    j = len(string)-1
    string_out = list(string)
    while string[i] == " " :
        i -= 1
    while i >= 0 :
        while string[i] != " " and i >= 0:
            string_out[j] = string[i]
            j -= 1
            i -= 1
        if i >= 0 :
            string_out[j] = "0"
            string_out[j-1] = "2"
            string_out[j-2] = "%"
            j -= 3
            i -= 1
    return ''.join(string_out)
