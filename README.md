
# Projeto CRUD Pokemon

Este é um projeto pequeno para praticar CRUD (Create, Read, Update, Delete) operations utilizando a python.

O projeto está dividido em 3 etapas:

1. **Console Interativo**: Nesta fase inicial, o projeto consiste em um console interativo onde é possível criar, atualizar, deletar e listar informações sobre Pokémon. Os dados são armazenados temporariamente na memória.

2. **Persistência de Dados**: Na segunda etapa, será adicionado um banco de dados para persistir os dados dos Pokémon. Isso permitirá que as informações dos Pokémon sejam mantidas entre diferentes execuções do programa.

3. **API (FastAPI)**: Na terceira e última etapa, será construída uma API utilizando o framework FastAPI. Esta API fornecerá endpoints para realizar operações CRUD com os Pokémon, permitindo que outras aplicações possam interagir com os dados.

## Requisitos

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/#installing-with-pipx)


## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/jvras58/Poke-api.git
   ```
   ou 
    ```bash
   git clone git@github.com:jvras58/Poke-api.git
   ```

## Uso

1. Para entrar no ambiente virtual do [Poetry](https://python-poetry.org/docs/#installing-with-pipx).

   ```bash
   poetry shell
   ```
   instale as dependencias:

   ```bash
   poetry install
   ```

3. Para executar o console interativo:
   ```bash
   task run
   ```
