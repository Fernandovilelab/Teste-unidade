class Fila:
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("Fila vazia")
        return self.items.pop(0)

    def esta_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

    def frente(self):
        if self.esta_vazia():
            raise IndexError("Fila vazia")
        return self.items[0]

