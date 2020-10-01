def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_mac_char_on_end(str):
    lenstr = ft_len(str)
    word = ""
    nword = ""
    count = 1
    mxcount = 0
    for i in range(lenstr):
        nword = str[i]
        if word == nword:
            count += 1
            word = nword
            if mxcount < count:
                mxcount = count
        else:
            word = nword
            if mxcount < count:
                mxcount = count
            count = 1
    return mxcount




