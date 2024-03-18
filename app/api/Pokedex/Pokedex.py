from app.api.Pokemon.Pokemon import Pokemon


class Pokedex:
    def __init__(self):
        """
        inicializa a Pokedex com uma lista vazia de pokemons.
        """
        self.pokemons = []

    def adicionar_pokemon(
        self,
        nome,
        tipo,
        regiao,
        habilidades,
        pode_evoluir,
        proxima_evolucao=None,
        evolucao=None,
    ):
        """
        Adiciona um novo Pokémon à Pokédex.

        Args:
            nome (str): O nome do Pokémon.
            tipo (str): O tipo do Pokémon.
            regiao (str): A região de origem do Pokémon.
            habilidades (list): Uma lista de habilidades do Pokémon.
            pode_evoluir (bool): Indica se o Pokémon pode evoluir.
            proxima_evolucao (str, optional): O nome da próxima evolução do Pokémon.
            evolucao (str, optional): O nome do Pokémon evoluído.
        """
        pokemon = Pokemon(
            nome,
            tipo,
            regiao,
            habilidades,
            pode_evoluir,
            proxima_evolucao,
            evolucao,
        )
        self.pokemons.append(pokemon)
        print(f'Pokemon: {pokemon.nome} adicionado com sucesso!')

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
                print(f'Pokemon: {pokemon.nome} atualizado com sucesso!')
                return
        print(f'Pokemon: {nome} não encontrado.')

    def remover_pokemon(self, nome):
        """
        Remove um Pokémon da Pokédex.

        Args:
            nome (str): O nome do Pokémon.
        """
        for pokemon in self.pokemons:
            if pokemon.nome == nome:
                self.pokemons.remove(pokemon)
                print(f'Pokemon: {pokemon.nome} removido com sucesso!')
                return

    def mostrar_pokemons(self):
        """
        Lista os Pokémons da Pokédex.
        """
        print(
            """
            ░█████╗░░█████╗░████████╗░█████╗░██╗░░░░░░█████╗░░██████╗░░█████╗░██╗
            ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗██╔════╝░██╔══██╗╚═╝
            ██║░░╚═╝███████║░░░██║░░░███████║██║░░░░░██║░░██║██║░░██╗░██║░░██║░░░
            ██║░░██╗██╔══██║░░░██║░░░██╔══██║██║░░░░░██║░░██║██║░░╚██╗██║░░██║░░░
            ╚█████╔╝██║░░██║░░░██║░░░██║░░██║███████╗╚█████╔╝╚██████╔╝╚█████╔╝██╗
            ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░░╚════╝░╚═╝
                """
        )
        lista_pokemons = []
        for pokemon in self.pokemons:
            detalhes_pokemon = f"Nome: {pokemon.nome}, Tipo: {pokemon.tipo}, Região: {pokemon.regiao}, Habilidades: {pokemon.habilidades}, Evolução: {pokemon.evolucao if pokemon.evolucao else 'N/A'}"
            print(detalhes_pokemon)
            lista_pokemons.append(detalhes_pokemon)
        return lista_pokemons

    def verificar_pokemon(self, nome):
        """
        Verifica se um Pokémon existe na Pokédex.
        Args:
            nome (str): O nome do Pokémon.

        Returns:
            bool: True se o Pokémon existir, False caso contrário.
        """
        return nome in [pokemon.nome for pokemon in self.pokemons]

    # TODO: Implementar evulação de pokemons...
    def evoluir_pokemon(self, nome):
        """
        Evolui um Pokémon, se possível.
        Args:
            nome (str): O nome do Pokémon a ser evoluído.
        """
        for pokemon in self.pokemons:
            if pokemon.nome == nome:
                if pokemon.evolucao:
                    print(
                        f"Pokemon: {pokemon.nome} já evoluiu para {pokemon.evolucao}!"
                    )
                elif pokemon.pode_evoluir:
                    pokemon.evolucao = pokemon.proxima_evolucao
                    print(
                        f"Pokemon: {pokemon.nome} evoluiu para {pokemon.evolucao}!"
                    )
                else:
                    print(f"Pokemon: {pokemon.nome} não pode evoluir.")
                return
        print(f"Pokemon: {nome} não encontrado.")

    # TODO: implementar batalhas de pokemons...
    def batalhar_pokemons(self, nome_pokemon1, nome_pokemon2):
        """
        Realiza uma batalha entre dois Pokémons.
        Args:
            nome_pokemon1 (str): O nome do primeiro Pokémon.
            nome_pokemon2 (str): O nome do segundo Pokémon.
        """
        pokemon1 = None
        pokemon2 = None
        for pokemon in self.pokemons:
            if pokemon.nome == nome_pokemon1:
                pokemon1 = pokemon
            if pokemon.nome == nome_pokemon2:
                pokemon2 = pokemon
        if pokemon1 and pokemon2:
            print(f"Batalha entre {pokemon1.nome} e {pokemon2.nome}!")
            if pokemon1.tipo == pokemon2.tipo:
                print("Empate!")
            elif pokemon1.tipo == "Fogo" and pokemon2.tipo == "Água":
                print(f"{pokemon2.nome} venceu!")
            elif pokemon1.tipo == "Água" and pokemon2.tipo == "Planta":
                print(f"{pokemon2.nome} venceu!")
            elif pokemon1.tipo == "Planta" and pokemon2.tipo == "Fogo":
                print(f"{pokemon2.nome} venceu!")
            else:
                print(f"{pokemon1.nome} venceu!")
        else:
            print("Pokémon não encontrado.")
