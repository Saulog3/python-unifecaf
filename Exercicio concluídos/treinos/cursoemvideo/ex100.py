from random import randint
from time import sleep


def aleatorio():
  

    lista = []
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(0,10)
        lista.append(num)
        print(f'{num}', end=' ',flush=True)
        sleep(0.5)

    print('Pronto!')
    print(lista)
    return lista


def somaPar(lst):
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma = num + soma
    print(f'Somando os valores pares de {lst}, temos {soma}')

nums = aleatorio()
somaPar(nums)

# ts=[]
# for i in range(0,10):
#     t = randint(0,10)
#     ts.append(t)

# print(ts)