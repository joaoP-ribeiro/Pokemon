from Tipo import Tipo
import random


class Monstro(Tipo):
    def __init__(self, tipo, nome, vida, ataque, velocidade, ataque1, ataque2, bot=False) -> None:
        super().__init__(tipo)
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.velocidade = velocidade
        self.ataque1 = ataque1
        self.ataque2 = ataque2
        self.bot = bot

    def perca_vida(self, dano, tipo):
        """
        Esse metodo retorna a vida do meu pokemon logo após o dano causado a ele
        :param dano: double
        :param tipo: str
        :return: double
        """
        dano = self.fraqueza(dano, tipo)
        print(f"Dano tomado é: {dano}")
        self.vida -= dano
        return self.vida

    def ataque_normal(self, vida_oponente):
        """
        Ataque normal que retorna um tipo normal,
        causa dano baseado na vida máxima do pokemon inimigo
        :param vida_oponente: double
        :return: double, str
        """
        print(f"{self.nome} usou {self.ataque1}")
        dano_i = (self.ataque * 0.1) * (vida_oponente / 10)
        dano_f = self.logica_dano(dano_i)
        return dano_f, "normal"

    def ataque_tipo(self, vida_maxima, vida_atual):
        """
        Ataque de tipo que retorna o tipo do pokemon que usa esse movimento,
        causa dano na vida perdida
        do pokemon inimigo
        :param vida_maxima: double
        :param vida_atual: double
        :return: double, str
        """
        print(f"{self.nome} usou {self.ataque2}")
        dano_i = (self.ataque * 0.2) + (self.velocidade * 0.1) + ((vida_maxima - vida_atual) * 0.4)
        dano_f = self.logica_dano(dano_i)
        return dano_f, self.tipo

    def logica_dano(self, dano):
        """
        Retorna o dano do ataque, pode retornar o mesmo valor que entrou, o dobro do valor de entrada
        ou zero
        :param dano: double
        :return: double
        """
        sorteio = [1, 2, 3]
        probabilidade = [0.7, 0.2, 0.1]
        sorteio = random.choices(sorteio, weights=probabilidade, k=1)[0]
        if sorteio == 1:
            print("Ataque bem sucedido")
            dano = dano
        elif sorteio == 2:
            print("Ataque crítico")
            dano = dano * 2
        else:
            print("Errou o ataque")
            dano = 0
        return dano

    def status_atual(self):
        print(f"{self.nome}: ")
        print(f"Vida: {self.vida}")

    def status(self):
        """
        printa os status do pokemon
        :return: None
        """
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Velocidade: {self.velocidade}")




