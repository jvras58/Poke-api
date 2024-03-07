from Pokedex import Pokedex

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
        print("\n1. Adicionar Pokemon")
        print("2. Mostrar Pokemons")
        print("3. Atualizar Pokemon")
        print("4. Remover Pokemon")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            nome = input("Digite o nome do Pokemon: ")
            tipo = input("Digite o tipo do Pokemon: ")
            regiao = input("Digite a região do Pokemon: ")
            habilidades = input("Digite as habilidades do Pokemon (separadas por vírgula): ").split(',')
            pokedex.adicionar_pokemon(nome, tipo, regiao, habilidades)
        elif opcao == '2':
            pokedex.mostrar_pokemons()
        elif opcao == '3':
            nome = input("Digite o nome do Pokemon: ")
            tipo = input("Digite o tipo do Pokemon: ")
            regiao = input("Digite a região do Pokemon: ")
            habilidades = input("Digite as habilidades do Pokemon (separadas por vírgula): ").split(',')
            pokedex.atualizar_pokemon(nome, tipo, regiao, habilidades)
        elif opcao == '4':
            nome = input("Digite o nome do Pokemon: ")
            pokedex.remover_pokemon(nome)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()