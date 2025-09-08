def numerospares(numero):
    listacompares = []
    for n in range(numero + 1):
        if n % 2 == 0:
            listacompares.append(n)
    return listacompares

n = int(input('Numero: '))
print(numerospares(n))