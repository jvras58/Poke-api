from api.Pokedex.Pokedex import Pokedex

# TODO: verificar melhorias na exibição e na construção do codigo do menu...
def mostrar_pokemons_e_menu(pokedex):
    """
    Exibe um menu secundario de opções para interagir com a Pokedex.

    Opções disponíveis:
    1. Voltar ao menu principal
    2. Sair
    """
    pokedex.mostrar_pokemons()
    while True:
        print(
            """
        1. Voltar ao menu principal
        2. Sair
        """
        )
        opcao = input('Escolha uma opção:')
        if opcao == '1':
            return
        elif opcao == '2':
            exit(0)
        else:
            print('Opção inválida. Tente novamente.')


def menu():
    """
    Exibe um menu de opções para interagir com a Pokedex.

    Opções disponíveis:
    1. Adicionar Pokemon
    2. Mostrar Pokemons
    3. Atualizar Pokemon
    4. Remover Pokemon
    5. Sair
    """
    pokedex = Pokedex()
    while True:
        print(
            """

    ██████╗░░█████╗░██╗░░██╗███████╗██████╗░███████╗██╗░░██╗
    ██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔════╝╚██╗██╔╝
    ██████╔╝██║░░██║█████═╝░█████╗░░██║░░██║█████╗░░░╚███╔╝░
    ██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██║░░██║██╔══╝░░░██╔██╗░
    ██║░░░░░╚█████╔╝██║░╚██╗███████╗██████╔╝███████╗██╔╝╚██╗
    ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝

        1. Adicionar Pokemon
        2. Mostrar Pokemons
        3. Atualizar Pokemon
        4. Remover Pokemon
        5. Sair
        """
        )
        opcao = input('Escolha uma opção:')
        print(f'Você escolheu a opção: {opcao}')
        if opcao == '1':
            nome = input('Digite o nome do Pokemon: ')
            if pokedex.verificar_pokemon(nome):
                print(f'Pokemon: {nome} já existe.')
                continue
            tipo = input('Digite o tipo do Pokemon: ')
            regiao = input('Digite a região do Pokemon: ')
            habilidades = input(
                'Digite as habilidades do Pokemon (separadas por vírgula): '
            ).split(',')
            pokedex.adicionar_pokemon(nome, tipo, regiao, habilidades)
        elif opcao == '2':
            mostrar_pokemons_e_menu(pokedex)
        elif opcao == '3':
            nome = input('Digite o nome do Pokemon: ')
            if not pokedex.verificar_pokemon(nome):
                print(f'Pokemon: {nome} não encontrado.')
            else:
                tipo = input('Atualize o tipo do Pokemon: ')
                regiao = input('Atualize a região do Pokemon: ')
                habilidades = input(
                    'Atualize as habilidades do Pokemon (separadas por vírgula): '
                ).split(',')
                pokedex.atualizar_pokemon(nome, tipo, regiao, habilidades)
        elif opcao == '4':
            nome = input('Digite o nome do Pokemon: ')
            if not pokedex.verificar_pokemon(nome):
                print(f'Pokemon: {nome} não encontrado.')
            pokedex.remover_pokemon(nome)
        elif opcao == '5':
            break
        else:
            print('Opção inválida. Tente novamente.')


menu()
