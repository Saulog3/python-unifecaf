# Retorne todos os números repetidos de uma lista de números # Exemplo: # Entrada: [6, 1, 1, 7, 2 , 6, 1] # Saída Esperada: [6, 1]
def numeros_repetidos(lista):
    repetidos = []
    vistos = set()

    for num in lista:
        if lista.count(num) > 1 and num not in vistos: #lista.count(num) → conta quantas vezes o número aparece.
            repetidos.append(num)
            vistos.add(num)

    return repetidos


# Testando
print(numeros_repetidos([6, 1, 1, 7, 2, 6, 1]))  # Saída esperada: [6, 1]
print(numeros_repetidos([4, 5, 6, 7]))           # Saída esperada: []
print(numeros_repetidos([2, 2, 2, 2]))           # Saída esperada: [2]