def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_first_end_three(str):
    newstr = ""
    if ft_len(str) > 5:
        for i in range(3):
            newstr += str[i]
        for i in range(ft_len(str) - 3, ft_len(str)):
            newstr += str[i]
        return newstr
    else:
        return str[0] * ft_len(str)



