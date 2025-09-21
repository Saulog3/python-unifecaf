# Retorne apenas os números pares de uma lista de números
# Exemplo:
#   Entrada: [9, 4, 7 , 2, 1]
#   Saída Esperada: [4, 2]

lista = [9, 4, 7, 2, 1]
saida = []
def filtro(lista):
    for i in (lista):
        if i % 2 == 0:
            saida.append(i)
    return saida


process = filtro(lista)

print(process)

