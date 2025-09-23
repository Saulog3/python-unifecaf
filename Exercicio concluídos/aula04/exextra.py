# with open('notas.txt', 'w') as f:
#     f.write('8.5\n')
#     f.write('7.0\n')
#     f.write('9.2\n')

# with open('notas.txt', 'r') as f:
#     for linha in f:
#         print(f'Notas: {linha.strip()}')
def ler_notas(arquivo):
    notas = []

    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    for linha in linhas:
        notas.append(float(linha.strip()))
    return notas


def calcular_media(notas):
    """Calcula a média de uma lista de notas"""
    return sum(notas) / len(notas) if notas else 0


def main():
    arquivo = "notas.txt"
    notas = ler_notas(arquivo)
    media = calcular_media(notas)

    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")


if __name__ == "__main__":
    main()
