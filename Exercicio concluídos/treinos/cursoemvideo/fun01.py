def fundob (lista):
    dobra = []
    for i in lista:
        d = i * 2
        dobra.append(d)
    print(dobra)


def dobra (lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1

# desempacotamento:

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(78,76,43,2,34,5)