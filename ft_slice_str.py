def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_slice_str(str, start, end):
    result = ""
    if end > ft_len(str):
        end = ft_len(str)
    for i in range(start - 1, end):
        result += str[i]
    return result


