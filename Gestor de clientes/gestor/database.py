class Clientes:
    # Lista de clientes
    lista = []
    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Clientes(dni, nombre, apellido)   #cliente
        Clientes.lista.append(cliente)
        return cliente
    @staticmethod
    def modificar(dni, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
        return Clientes.lista[i]
    @staticmethod
    def borrar(dni):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(i)
        return cliente