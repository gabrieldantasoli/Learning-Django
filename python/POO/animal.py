import abc

class Animal(abc.ABC):
    def __init__(self, nome, cor, idade):
        self._nome = nome
        self._cor = cor
        self._idade = idade
        self._especial = "Ain Ain"
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, cor):
        self._cor = cor
        
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
        
    @abc.abstractclassmethod
    def comer(self):
        pass