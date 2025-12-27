

def fatorial (num, show=False):
    f = 1 #multiplicador

    for i in range(num, 0, -1):
        if show:
            print(i, end=' ')
            if i > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')

        f *= i
    return f

        
print(fatorial(8, True))
        




 