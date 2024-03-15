from app.api.Pokedex.Pokedex import Pokedex

# executa o teste: pytest tests/test_Pokedex.py

# TODO: Implementar as fixtures para os testes de Pokedex (Don't repeat yourself)


def test_adicionar_pokemon():
    """
    Testa o método adicionar_pokemon da classe Pokedex.

    Verifica se o método adiciona corretamente um novo Pokemon à Pokedex,
    verificando se o tamanho da lista de pokemons é igual a 1 e se as
    propriedades do Pokemon adicionado estão corretas.

    """
    pokedex = Pokedex()
    pokedex.adicionar_pokemon(
        'Pikachu', 'Elétrico', 'Kanto', ['Choque do Trovão']
    )
    assert len(pokedex.pokemons) == 1
    assert pokedex.pokemons[0].nome == 'Pikachu'
    assert pokedex.pokemons[0].tipo == 'Elétrico'
    assert pokedex.pokemons[0].regiao == 'Kanto'
    assert pokedex.pokemons[0].habilidades == ['Choque do Trovão']
    assert pokedex.pokemons[0].evolucao is None
    assert 'Pokemon: Pikachu adicionado com sucesso!'


def test_atualizar_pokemon():
    """
    Testa o método atualizar_pokemon da classe Pokedex.

    Verifica se o método `atualizar_pokemon` atualiza corretamente as informações de um Pokémon na Pokedex.
    O teste adiciona um Pokémon à Pokedex, chama o método `atualizar_pokemon` para atualizar suas informações
    e verifica se as informações foram atualizadas corretamente.
    """
    pokedex = Pokedex()
    pokedex.adicionar_pokemon(
        'Pikachu', 'Elétrico', 'Kanto', ['Choque do Trovão']
    )
    pokedex.atualizar_pokemon(
        'Pikachu', 'Elétrico', 'Kanto', ['Choque do Trovão', 'Cauda de Ferro']
    )
    assert len(pokedex.pokemons) == 1
    assert pokedex.pokemons[0].nome == 'Pikachu'
    assert pokedex.pokemons[0].tipo == 'Elétrico'
    assert pokedex.pokemons[0].regiao == 'Kanto'
    assert pokedex.pokemons[0].habilidades == [
        'Choque do Trovão',
        'Cauda de Ferro',
    ]
    assert pokedex.pokemons[0].evolucao is None
    assert 'Pokemon: Pikachu atualizado com sucesso!'


def test_atualizar_pokemon_nao_encontrado():
    """
    Testa o método atualizar_pokemon da classe Pokedex.

    Verifica se o método `atualizar_pokemon` retorna uma mensagem de erro quando o Pokemon não é encontrado.
    O teste chama o método `atualizar_pokemon` para atualizar as informações de um Pokemon que não está na Pokedex.
    """
    pokedex = Pokedex()
    pokedex.atualizar_pokemon(
        'Pikachu', 'Elétrico', 'Kanto', ['Choque do Trovão']
    )
    assert 'Pokemon: Pikachu não encontrado.'


def test_remover_pokemon():
    """
    Teste para o método `remover_pokemon` da classe Pokedex.

    O teste adiciona um Pokémon à Pokedex, chama o método `remover_pokemon` que
    deve remover Pikachu da pokedex.
    """
    pokedex = Pokedex()
    pokedex.adicionar_pokemon(
        'Pikachu', 'Elétrico', 'Kanto', ['Choque do Trovão']
    )
    pokedex.remover_pokemon('Pikachu')
    assert len(pokedex.pokemons) == 0
    assert 'Pokemon: Pikachu removido com sucesso!'


def test_mostrar_pokemons():
    """
    Teste para o método `mostrar_pokemons` da classe Pokedex.

    Verifica se o método `mostrar_pokemons` retorna uma lista de pokemons
    deve incluir Pikachu, Charmander e Squirtle.
    """
    pokedex = Pokedex()
    pokedex.adicionar_pokemon(
        'Pikachu', 'Elétrico', 'Kanto', ['Choque do Trovão']
    )
    pokedex.adicionar_pokemon('Charmander', 'Fogo', 'Kanto', ['Brasas'])
    pokedex.adicionar_pokemon('Squirtle', 'Água', 'Kanto', ['Jato de Água'])
    pokemons = pokedex.mostrar_pokemons()
    assert any('Pikachu' in pokemon for pokemon in pokemons)
    assert any('Charmander' in pokemon for pokemon in pokemons)
    assert any('Squirtle' in pokemon for pokemon in pokemons)


def test_verificar_pokemon():
    """
    Testa o método `verificar_pokemon` da classe Pokedex.

    Verifica se o método `verificar_pokemon` retorna True para um Pokemon que está na Pokedex e False para um Pokemon que não está na Pokedex.
    """
    pokedex = Pokedex()
    pokedex.adicionar_pokemon(
        'Pikachu', 'Elétrico', 'Kanto', ['Choque do Trovão']
    )
    assert pokedex.verificar_pokemon('Pikachu') is True
    assert pokedex.verificar_pokemon('Charmander') is False
    assert pokedex.verificar_pokemon('Squirtle') is False
