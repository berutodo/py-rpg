import random

class Personagem:
    def __init__(self, nome, pontos_vida, poder_ataque, poder_defesa):
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.poder_ataque = poder_ataque
        self.poder_defesa = poder_defesa

    def atacar(self, alvo):
        dano = random.randint(1, self.poder_ataque)
        alvo.defender(dano)

    def defender(self, dano):
        defesa = random.randint(1, self.poder_defesa)
        dano_recebido = max(0, dano - defesa)
        self.pontos_vida -= dano_recebido

    def esta_vivo(self):
        return self.pontos_vida > 0

def batalha(personagem, oponente):
    while personagem.esta_vivo() and oponente.esta_vivo():
        print(f"{personagem.nome} - PV: {personagem.pontos_vida} | {oponente.nome} - PV: {oponente.pontos_vida}")
        # Turno do personagem
        personagem.atacar(oponente)
        if not oponente.esta_vivo():
            print(f"{oponente.nome} foi derrotado!")
            break
        oponente.atacar(personagem)
        if not personagem.esta_vivo():
            print(f"{personagem.nome} foi derrotado!")
            break