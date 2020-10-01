def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_reverse_str(str):
    res = ""
    for i in range(ft_len(str) - 1, -1, -1):
        res += str[i]
    return res


def ft_equal_reverse(str):
    revstr = ft_reverse_str(str)
    if revstr == str:
        return True
    return False
