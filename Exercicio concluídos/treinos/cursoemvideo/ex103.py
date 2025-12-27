def ficha(nome='<desconhecido>', gols=0):
    nome = input('Nome do Jogador: ')
    gols = input('Número de gols: ')
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'

print(ficha())


