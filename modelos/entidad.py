from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")

        self._nombre = valor

    @abstractmethod
    def mostrar_informacion(self):
        pass