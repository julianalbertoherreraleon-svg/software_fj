from abc import ABC, abstractmethod
from modelos.entidad import Entidad
from modelos.excepciones import ServicioError


class Servicio(Entidad, ABC):

    def __init__(self, nombre, precio_base):

        super().__init__(nombre)

        self._precio_base = precio_base

        if precio_base <= 0:
            raise ServicioError(
                "El precio base debe ser mayor que cero"
            )

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):

        if valor <= 0:
            raise ServicioError(
                "El precio debe ser positivo"
            )

        self._precio_base = valor

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass