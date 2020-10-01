def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_find_str(str1, str2):
    len1 = ft_len(str1)
    len2 = ft_len(str2)
    ismatch = True
    for i in range(0, (len1 - len2) + 1):
        ismatch = True
        for j in range(len2):
            if str1[i+j] != str2[j]:
                ismatch = False
                break
        if ismatch:
            return i + 1
    return -1







