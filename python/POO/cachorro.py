from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, cor, idade):
        super().__init__(nome, idade, cor)
    
    def latir(self):
        return "Au Au"
    
    