def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'

nome = input('Nome do Jogador: ')
gols = int(input('Número de gols: '))
print(ficha(nome, gols))