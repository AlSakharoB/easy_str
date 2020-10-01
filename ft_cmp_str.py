def ft_slice_str(str, start, end):
    result = ""
    if end > ft_len(str):
        end = ft_len(str)
    for i in range(start - 1, end):
        result += str[i]
    return result


def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_cmp_str(str1, str2, num):
    start = ft_slice_str(str1, 1, num - 1)
    end = ft_slice_str(str1, num, ft_len(str1))
    str3 = start + str2 + end
    return str3





