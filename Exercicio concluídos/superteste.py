import random

class Lutador:
    def __init__(self, nome, vida, força, ataques, defesas):
        self.nome = nome
        self.vida = vida
        self.força = força
        self.ataques = ataques
        self.defesas = defesas

    def escolher_ataque(self):
        return random.choice(list(self.ataques.items()))

    def escolher_defesa(self):
        return random.choice(list(self.defesas.items()))

    def receber_dano(self, dano):
        self.vida = max(self.vida - dano, 0)

def turno(atacante, defensor):
    nome_ataque, dano = atacante.escolher_ataque()
    nome_defesa, bloqueio = defensor.escolher_defesa()

    # Chance de crítico
    if random.random() < 0.2:
        dano *= 2
        print("💥  ATAQUE CRÍTICO!")

    dano_final = max(dano - random.randint(0, bloqueio), 0)
    defensor.receber_dano(dano_final)

    print(f"\n{atacante.nome} usou {nome_ataque} causando {dano} de dano.")
    print(f"{defensor.nome} tentou {nome_defesa} e bloqueou {bloqueio}.")
    print(f"Dano final em {defensor.nome}: {dano_final}")
    print(f"Vida de {defensor.nome}: {defensor.vida}")

def luta(lutador1, lutador2):
    turno_atual = 0
    while lutador1.vida > 0 and lutador2.vida > 0:
        print(f"\n--- Turno {turno_atual + 1} ---")
        if turno_atual % 2 == 0:
            turno(lutador1, lutador2)
        else:
            turno(lutador2, lutador1)
        turno_atual += 1

    vencedor = lutador1 if lutador1.vida > 0 else lutador2
    print(f"\n🏆 {vencedor.nome} venceu a luta!")

# Criando os lutadores
goku = Lutador("Goku", 100, 50, {"soco": 10, "disparo_ki": 15, "kamehamha": 50}, {"fechar_guarda": 5, "desvio": 7})
vegeta = Lutador("Vegeta", 120, 60, {"soco": 10, "disparo_ki": 15, "garlic_gun": 50}, {"fechar_guarda": 5, "desvio": 7})

# Iniciar a luta
luta(goku, vegeta)
