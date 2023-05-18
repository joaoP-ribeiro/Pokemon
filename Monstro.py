from Tipo import Tipo
import random


class Monstro(Tipo):
    def __init__(self, tipo, nome, vida, ataque, velocidade, rosto, ataque1, ataque2, bot=False) -> None:
        super().__init__(tipo)
        self._nome = nome
        self._vida = vida
        self._vida_maxima = vida
        self.ataque = ataque
        self.velocidade = velocidade
        self._rosto = rosto
        self._ataque1 = ataque1
        self._ataque2 = ataque2
        self.bot = bot

    @property
    def nome(self):
        return self._nome
    
    @property
    def vida(self):
        return self._vida
    
    @property
    def vida_maxima(self):
        return self._vida_maxima
    
    @property
    def rosto(self):
        return self._rosto
    
    @property
    def ataque1(self):
        return self._ataque1
    
    @property
    def ataque2(self):
        return self._ataque2

    def perca_vida(self, dano, tipo):
        """
        Esse metodo retorna a vida do meu pokemon logo após o dano causado a ele
        :param dano: double
        :param tipo: str
        :return: double
        """
        dano = self.fraqueza(dano, tipo)
        return dano


    def ataque_normal(self, vida_oponente):
        """
        Ataque normal que retorna um tipo normal,
        causa dano baseado na vida máxima do pokemon inimigo
        :param vida_oponente: double
        :return: double, str
        """
        dano_i = (self.ataque * 0.1) * (vida_oponente / 10)
        dano_f, fraze = self.logica_dano(dano_i)
        return dano_f, "normal", fraze

    def ataque_tipo(self, vida_maxima, vida_atual):
        """
        Ataque de tipo que retorna o tipo do pokemon que usa esse movimento,
        causa dano na vida perdida
        do pokemon inimigo
        :param vida_maxima: double
        :param vida_atual: double
        :return: double, str
        """
        dano_i = (self.ataque * 0.2) + (self.velocidade * 0.1) + ((vida_maxima - vida_atual) * 0.4)
        dano_f, fraze = self.logica_dano(dano_i)
        return dano_f, self.tipo, fraze

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
            dano = dano
            return dano, "Ataque bem sucedido"
        elif sorteio == 2:
            print("Ataque crítico")
            dano = dano * 2
            return dano, "Ataque crítico"
        else:
            dano = 0
            return dano, "Errou o ataque"

    @vida.setter
    def vida(self, value):
        self._vida = value





