from objetos.Animal import Animal
from objetos.Cachorro import Cachorro
from objetos.Gato import Gato

cachorro1 = Cachorro('Theodoro', 2, 'Vira-lata', 0)
cachorro1.emitir_som()
print(cachorro1)
cachorro1.exibir_detalhes()
print('************************')
gato1 = Gato('Leonardo', 3, 'Persa', 4000)
gato1.emitir_som()
print(gato1)
gato1.exibir_detalhes()