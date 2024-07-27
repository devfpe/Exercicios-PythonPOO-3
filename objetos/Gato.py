from objetos.Animal import Animal

class Gato(Animal):
    def __init__(self, nome: str, idade: int, raca: str, preco: float):
        super().__init__(nome, idade)
        self._raca: str = raca
        self._preco: float = preco

    def exibir_detalhes(self):
        print(f'Raça: {self._raca} | Preço: R${self._preco}')    
        
    def emitir_som(self):
        print('meow meooow')