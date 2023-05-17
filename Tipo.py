class Tipo():
    def __init__(self, tipo) -> None:
        self.tipo = tipo

    def fraqueza(self, dano, tipo="normal"):
        """
        Define o dano recebido de acordo com a fraqueza desse pokemon
        e o tipo do ataque do pokemon inimigo
        :param dano: double
        :param tipo: str
        :return: double
        """
        if self.tipo == "agua":
            if tipo == "fogo":
                dano = dano * 0.5
            elif tipo == "planta":
                dano = dano * 2
        elif self.tipo == "planta":
            if tipo == "agua":
                dano = dano * 0.5
            elif tipo == "fogo":
                dano = dano * 2
        else:
            if tipo == "planta":
                dano = dano * 0.5
            elif tipo == "agua":
                dano = dano * 2
        return dano


