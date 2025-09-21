# Retorne todos os números exitentes em ambas as listas
# Exemplo:
#   Entrada: 
#       ListaA = [4, 9, 3 , 7, 8]
#       Listab = [9, 5, 4 , 2, 1]
#   Saída Esperada: [9, 4]


def numeros_comuns(listaA, listaB):
    comuns = []
    for i in range(len(listaA)):
        if listaA[i] in listaB and listaA[i] not in comuns:
            comuns.append(listaA[i])
    return comuns


# Testando
listaA = [4, 9, 3, 7, 8, 9 ,2]
listaB = [9, 5, 4, 2, 1]

print(numeros_comuns(listaA, listaB))  # [4, 9]
