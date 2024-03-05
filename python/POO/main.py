from cachorro import Cachorro
from gato import Gato

cachorro1 = Cachorro("Toto", "Preto", 4, "gabriel")
gato1 = Gato("Simba", "Branco", 3)


print(gato1.nome)
print(gato1.miar())
print("-----------------------------")

cachorro1.dono = "Samuel"
print(cachorro1.nome)
# print(cachorro1._Cachorro__dono)
print(cachorro1.dono)
print(cachorro1.latir())
print(cachorro1.chorar())
print(cachorro1.comer())