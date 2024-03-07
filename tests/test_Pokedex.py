from app.api.Pokedex.Pokedex import Pokedex

def test_adicionar_pokemon():
    pokedex = Pokedex()
    pokedex.adicionar_pokemon("Pikachu", "Elétrico", "Kanto", ["Choque do Trovão"])
    assert len(pokedex.pokemons) == 1
    assert pokedex.pokemons[0].nome == "Pikachu"
    assert pokedex.pokemons[0].tipo == "Elétrico"
    assert pokedex.pokemons[0].regiao == "Kanto"
    assert pokedex.pokemons[0].habilidades == ["Choque do Trovão"]
    assert pokedex.pokemons[0].evolucao is None
    assert f"Pokemon: Pikachu adicionado com sucesso!"
