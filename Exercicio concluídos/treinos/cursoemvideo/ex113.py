def leiaInt(mensagem):
 


    while True:

        try:
            n = int(input(mensagem))

        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número válido!.\033[m')

        except KeyboardInterrupt:
            print('Nenhum dado recebido')
            return 0
           
        except Exception as erro:
            print(f'Erro de {erro.__class__}')

        else:

            break
    return n
 

n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')