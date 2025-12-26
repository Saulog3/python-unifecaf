from time import sleep
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def contador(inicio, fim, passo):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for i in lst:
        print(i, end=' ')
    print('Fim!\n')

    for i in range(len(lista), 0, -2):
        print(i, end=" ")
    print('Fim!')
    
    if inicio < fim:
        for n in range( inicio, fim + passo, passo):
                print(n, end=' ')
    else:
        for n in range(fim, inicio, passo):
            print(n, end=' ')



print('Agora é sua vez de personalizar a contagem: ')
ini = int(input('Início: '))
fm = int(input('Fim: '))
passo = int(input('Passo: '))



contador(ini, fm, passo)