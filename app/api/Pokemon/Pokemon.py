class Pokemon:
    """
    Representa o Pokemon.

    Args:
        nome (str): o nome do Pokemon.
        tipo (str): o tipo do Pokemon.
        regiao (str): a região do Pokemon.
        habilidades (list): a lista de habilidades do pokemon.
        pode_evoluir (bool): indica se o pokemon pode evoluir.
        proxima_evolucao (str, optional): o nome da próxima evolução do pokemon.
        evolucao (str, optional): status de evolução.
    """

    def __init__(
        self,
        nome,
        tipo,
        regiao,
        habilidades,
        pode_evoluir,
        proxima_evolucao=None,
        evolucao=None,
    ):
        self.nome = nome
        self.tipo = tipo
        self.regiao = regiao
        self.habilidades = habilidades
        self.pode_evoluir = pode_evoluir
        self.proxima_evolucao = proxima_evolucao
        self.evolucao = evolucao
