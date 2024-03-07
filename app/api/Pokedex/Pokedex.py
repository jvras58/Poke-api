
from Pokemon.Pokemon import Pokemon


class Pokedex:
    def __init__(self):
        """
        inicializa a Pokedex com uma lista vazia de pokemons.
        """
        self.pokemons = []

    def adicionar_pokemon(self, nome, tipo, regiao, habilidades, evolucao=None):
            """
            Adiciona um novo Pokémon à Pokédex.

            Args:
                nome (str): O nome do Pokémon.
                tipo (str): O tipo do Pokémon.
                regiao (str): A região de origem do Pokémon.
                habilidades (list): Uma lista de habilidades do Pokémon.
                evolucao (str, optional): O nome do Pokémon evoluído.
            """
            pokemon = Pokemon(nome, tipo, regiao, habilidades, evolucao)
            self.pokemons.append(pokemon)
            print(f"Pokemon: {pokemon.nome} adicionado com sucesso!")

    def atualizar_pokemon(self, nome, tipo, regiao, habilidades):
        """
        Atualiza um Pokémon da Pokédex.

        Args:
            nome (str): O nome do Pokémon.
            tipo (str): O tipo do Pokémon.
            regiao (str): A região de origem do Pokémon.
            habilidades (list): Uma lista de habilidades do Pokémon.
            evolucao (str, optional): O nome do Pokémon evoluído.
        """
        for pokemon in self.pokemons:
            if pokemon.nome == nome:
                pokemon.tipo = tipo
                pokemon.regiao = regiao
                pokemon.habilidades = habilidades
                print(f"Pokemon: {pokemon.nome} atualizado com sucesso!")
                return
        print(f"Pokemon: {nome} não encontrado.")

    def remover_pokemon(self, nome):
        """
        Remove um Pokémon da Pokédex.

        Args:
            nome (str): O nome do Pokémon.
        """
        for pokemon in self.pokemons:
            if pokemon.nome == nome:
                self.pokemons.remove(pokemon)
                print(f"Pokemon: {pokemon.nome} removido com sucesso!")
                return

    def mostrar_pokemons(self):
        """
        Lista os Pokémons da Pokédex.
        """
        print("Lista de Pokemons:")
        for pokemon in self.pokemons:
            print(f"Nome: {pokemon.nome}, Tipo: {pokemon.tipo}, Região: {pokemon.regiao}, Habilidades: {pokemon.habilidades}, Evolução: {pokemon.evolucao.nome if pokemon.evolucao else 'N/A'}")

    def verificar_pokemon(self, nome):
        """
        Verifica se um Pokémon existe na Pokédex.

        Args:
            nome (str): O nome do Pokémon.

        Returns:
            bool: True se o Pokémon existir, False caso contrário.
        """
        return nome in [pokemon.nome for pokemon in self.pokemons]
