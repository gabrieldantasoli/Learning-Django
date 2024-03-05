from animal import Animal

class Gato(Animal):
    def __init__(self, nome, cor, idade):
        super().__init__(nome, idade, cor)
        
    def miar(self):
        return "Miau"