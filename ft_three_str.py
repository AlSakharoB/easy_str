def ft_slice_str(str, start, end):
    result = ""
    if end > ft_len(str):
        end = ft_len(str)
    for i in range(start - 1, end):
        result += str[i]
    return result


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


def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_three_str(str1, str2, str3):
    resstr = str1
    strslice = 0
    len1 = ft_len(str1)
    len2 = ft_len(str2)
    while ft_find_str(resstr, str2) != -1:
        strslice = ft_find_str(resstr, str2) - 1
        resstr = ft_slice_str(resstr, 1, strslice) + str3 + (ft_slice_str(resstr, strslice + len2 + 1, len1))
    return resstr

