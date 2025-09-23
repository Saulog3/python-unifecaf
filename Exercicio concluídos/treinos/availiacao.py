def soma_par(num):
    lista_pares = []
    i = 0

    while i <= num:
        if i % 2 == 0:
            lista_pares.append(i)
        i += 1
    return sum(lista_pares)


numero = int(input('Numero: '))
result = soma_par(numero)
print(f'O total é {result}') 
