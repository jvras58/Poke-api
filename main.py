class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Pedido:
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens

class Restaurante:
    def __init__(self):
        self.clientes = []
        self.pedidos = []

    def adicionar_cliente(self, nome, telefone):
        cliente = Cliente(nome, telefone)
        self.clientes.append(cliente)
        print("Cliente adicionado com sucesso!")

    def fazer_pedido(self, cliente, itens):
        pedido = Pedido(cliente, itens)
        self.pedidos.append(pedido)
        print("Pedido realizado com sucesso!")

    def mostrar_clientes(self):
        print("Lista de Clientes:")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}, Telefone: {cliente.telefone}")

    def mostrar_pedidos(self):
        print("Lista de Pedidos:")
        for pedido in self.pedidos:
            print(f"Cliente: {pedido.cliente.nome}, Itens: {pedido.itens}")
            
restaurante = Restaurante()