def numerospares(numero):
    listacompares = []
    for n in range(len(numero)):
        if numero % 2 == 0:
            listacompares.append(numero)
    return listacompares


print(numerospares(n))