# Dada uma lista de números, calcule:
#   - a soma de todos os números
#   - a média de todos os números
#   - O maior número
#   - o menor número 


lista_numeros = [9, 1, 2, 3, 4, 5, 6]

def soma(lista_numeros: list):
    soma = 0
    for i in lista_numeros:
        soma = soma + i

    return soma

def calc_media(lista_numeros: list):
    media = soma(lista_numeros) / len(lista_numeros)
    return media

def find_bigger(lista_numeros):
    maior = 0
    for i in lista_numeros:
        if i > maior:
            maior = i
    return maior

def find_smaller(lista_numeros):
    menor = lista_numeros[0]
    for i in lista_numeros:
        if i < menor:
            menor = i
    return menor



print('Soma: ', soma(lista_numeros))
print('Média: ', calc_media(lista_numeros))
print('Maior: ', find_bigger(lista_numeros))
print('Menor: ',find_smaller(lista_numeros))
