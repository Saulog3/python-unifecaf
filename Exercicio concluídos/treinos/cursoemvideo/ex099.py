from time import sleep

def maior(* valor):
    cont = maior = 0
    print('Analisando os valores recebidos...')
    for i in valor:
        print(i, end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
            cont += 1
    print(f'foram informados {cont} ao todo.')
    print(f'O maior valor informado foi {maior}')

        



maior(10, 20, 30, 40)
maior(4)
maior()
