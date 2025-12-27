from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if p == 0:
         p = 1
    if p < 0:
        p = p * - 1

    if i < f:
        for n in range( i, f + p, p):
            print(n, end=' ', flush=True)
            sleep(0.5)
        print('Fim!')

    elif i > f:
        for n in range(i, f - p, - p):
            print(n, end=' ',flush=True)
            sleep(0.5)
        print('Fim!')


#Programa Principal
contador(1, 10, 1)
contador(20, 0, 2)
print('Agora é sua vez de personalizar a contagem: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))


contador(inicio, fim, passo)

