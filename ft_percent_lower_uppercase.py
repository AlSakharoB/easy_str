def ft_percent_lower_uppercase(x):
    a = 'qwertyuioplkjhgfdsazxcvbnm'
    A = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    b = 'ёйцукенгшщзхъэждлорпавыфячсмитьбю'
    B = 'ЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
    s = 0
    h = 0
    c = 0
    for i in x:
        if i in a or i in b:
            s += 1
        if i in A or i in B:
            h += 1
        c += 1
    if s / h == 1:
        return 1
    else:
        return s / h * 100

