from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, cor, idade, dono):
        super().__init__(nome, idade, cor)
        self.__dono = dono
        
    
    def latir(self):
        return "Au Au"
    
    def chorar(self):
        return self._especial
    
    def comer(self):
        print("Au comendo")