from app.startup import menu


def test_adicionar_pokemon(mock_input, capsys):
    """
    Testa a adição de um Pokemon.

    Este teste verifica se a função menu() adiciona corretamente um Pokemon.
    O teste simula a entrada do usuário para adicionar um Pokemon chamado Pikachu,
    do tipo Elétrico, da região de Kanto, com os movimentos Electric Shock e Thunderbolt,

    O teste verifica se o nome do Pokemon adicionado é exibido corretamente na saída.

    Parâmetros:
    - mock_input: objeto de simulação de entrada do usuário
    - capsys: objeto de captura de saída do console
    """
    mock_input.write(
        '1\nPikachu\nEletrico\nKanto\nElectric Shock, Thunderbolt\n5\n'
    )
    mock_input.seek(0)
    menu()
    captured = capsys.readouterr()
    assert 'Pikachu' in captured.out


def test_mostrar_pokemons(mock_input, capsys):
    """
    Testa a exibição de um Pokemon.

    Este teste verifica se a função menu() exibe corretamente um Pokemon.
    O teste simula a entrada do usuário para exibir os pokemons (como estã sem nenhum pokemon ele imprime uma lista vazia),

    O teste verifica (no caso se a lista e vazia) exibido corretamente na saída.

    Parâmetros:
    - mock_input: objeto de simulação de entrada do usuário
    - capsys: objeto de captura de saída do console
    """
    mock_input.write('2\n5\n1\n5\n')
    mock_input.seek(0)
    menu()
    captured = capsys.readouterr()
    assert (
        """
            ░█████╗░░█████╗░████████╗░█████╗░██╗░░░░░░█████╗░░██████╗░░█████╗░██╗
            ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗██╔════╝░██╔══██╗╚═╝
            ██║░░╚═╝███████║░░░██║░░░███████║██║░░░░░██║░░██║██║░░██╗░██║░░██║░░░
            ██║░░██╗██╔══██║░░░██║░░░██╔══██║██║░░░░░██║░░██║██║░░╚██╗██║░░██║░░░
            ╚█████╔╝██║░░██║░░░██║░░░██║░░██║███████╗╚█████╔╝╚██████╔╝╚█████╔╝██╗
            ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░░╚════╝░╚═╝
                """
        in captured.out
    )


def test_atualizar_pokemon(mock_input, capsys):
    """
    Testa a atualização de um Pokemon.

    Este teste verifica se a função `menu()` atualiza corretamente um Pokemon.
    O teste simula a entrada do usuário para atualizar um Pokemon específico
    e verifica se o nome do Pokemon atualizado é exibido corretamente na saída.

    Args:
        mock_input (io.StringIO): Objeto de entrada simulada.
        capsys (pytest.CaptureFixture): Objeto de captura de saída.

    """
    mock_input.write(
        '3\nPikachu\nCharizard\nFogo\nKanto\nFlamethrower, Fly\n5\n'
    )
    mock_input.seek(0)
    menu()
    captured = capsys.readouterr()
    assert 'Charizard' in captured.out


def test_remover_pokemon(mock_input, capsys):
    """
    Testa a remoção de um Pokemon.

    Este teste verifica se a função menu() remove corretamente um Pokemon quando o usuário seleciona a opção 4 e insere o nome do Pokemon a ser removido.
    O teste utiliza um objeto mock_input para simular a entrada do usuário, escrevendo "4", "pikachu" e "5" no buffer de entrada.
    Em seguida, o teste chama a função menu() e captura a saída usando o objeto capsys.
    Por fim, o teste verifica se a mensagem "Pokemon: pikachu não encontrado." está presente na saída capturada.

    """
    mock_input.write('4\npikachu\n5\n')
    mock_input.seek(0)
    menu()
    captured = capsys.readouterr()
    assert 'Pokemon: pikachu não encontrado.' in captured.out
