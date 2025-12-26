def terrenoCalc (largura, altura):
    calc = largura * altura
    print(f'A área do terrano {largura}x{altura} é de {calc}m²')


print('CONTROLE DE TERRENOS')
print('--------------------')
larg = float(input('Largura: '))
compr = float(input('Altura: '))

terrenoCalc(larg, compr)