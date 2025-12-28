

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

        
# print(fatorial(8, True))
        


f = 1
n = 10
while n != 0:
    print(n, end=' ')
    if n > 1:
        print(f' x ', end=' ')
    else:
        print(f' = ', end=' ')
    f *= n
    n -= 1

print(f'{f}')

 