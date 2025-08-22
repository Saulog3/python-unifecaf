# Implementação de função com filtro


lista_num = [1, 2, 3, 4, 5, 6]


# def funcao_filtro_par():
#     if num % 2 == 0:
#         lista_apos_filtro.append(num)
#         print('Numeros pares encontrados: ', lista_apos_filtro)
#     else:
#         print('Impar!')
def funcao_filtro_par(lista_apos_filtro):
    lista_apos_filtro = []
    for num in range(len(lista_num)):
        if lista_num[num] % 2 == 0:
            lista_apos_filtro.append(lista_num[num])
    return lista_apos_filtro
        
print('Numeros pares encontrados: ', funcao_filtro_par(lista_num))
