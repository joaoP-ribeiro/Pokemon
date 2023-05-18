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
            if tipo == "planta":
                dano = dano * 2
            else:
                dano = dano

        if self.tipo == "planta":
            if tipo == "agua":
                dano = dano * 0.5
            if tipo == "fogo":
                dano = dano * 2
            else:
                dano = dano

        if self.tipo == "fogo":
            if tipo == "planta":
                dano = dano * 0.5
            if tipo == "agua":
                dano = dano * 2
            else:
                dano = dano
        return dano


