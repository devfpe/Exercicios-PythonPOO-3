from abc import abstractmethod

class Animal:
    def __init__(self, nome: str, idade: int):
        self._nome: str = nome
        self._idade: int = idade

    def __str__(self) -> str:
        return f'Nome do animal: {self._nome} | Idade do animal: {self._idade} anos'

    @abstractmethod
    def emitir_som(self):
        pass