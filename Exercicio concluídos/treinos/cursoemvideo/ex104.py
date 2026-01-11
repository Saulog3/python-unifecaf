def leiaInt(mensagem):
    naoErro = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            naoErro = True
        else:
            print('\033[0;31mErro! Digite um número válido!.\033[m')
        if naoErro:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')