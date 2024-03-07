class Pokemon:
    """
    Representa o Pokemon.

    Args:
        nome (str): o nome do Pokemon.
        tipo (str): o tipo do Pokemon.
        regiao (str): a região do Pokemon.
        habilidades (list): a lista de habilidades do pokemon.
        evolucao (str, optional): status de evolução.
    """

    def __init__(self, nome, tipo, regiao, habilidades, evolucao=None):
        self.nome = nome
        self.tipo = tipo
        self.regiao = regiao
        self.habilidades = habilidades
        self.evolucao = evolucao
