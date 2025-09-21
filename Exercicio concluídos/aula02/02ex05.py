# Ordene a lista de forma crescente
# Exemplo:
#   Entrada: [5, 7, 2 , 1]
#   Saída Esperada: [1, 2, 5, 7]


def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


# Testando
print(ordenar_lista([5, 7, 2, 1]))  # [1, 2, 5, 7]


