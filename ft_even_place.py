def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_even_place(str):
    newstr = ""
    for i in range(ft_len(str)):
        if i % 2 == 1:
            newstr += str[i]
    return newstr


