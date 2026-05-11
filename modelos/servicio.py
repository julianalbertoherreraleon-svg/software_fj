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


class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, capacidad):

        super().__init__(nombre, precio_base)

        self.capacidad = capacidad

    def calcular_costo(self, horas=1):

        return self._precio_base * horas

    def mostrar_informacion(self):

        return (
            f"Servicio Sala: {self._nombre} | "
            f"Capacidad: {self.capacidad}"
        )


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, tipo_equipo):

        super().__init__(nombre, precio_base)

        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias=1):

        return self._precio_base * dias

    def mostrar_informacion(self):

        return (
            f"Equipo: {self._nombre} | "
            f"Tipo: {self.tipo_equipo}"
        )


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, especialista):

        super().__init__(nombre, precio_base)

        self.especialista = especialista

    def calcular_costo(self, horas=1, descuento=0):

        total = self._precio_base * horas

        if descuento > 0:
            total -= total * descuento

        return total

    def mostrar_informacion(self):

        return (
            f"Asesoría: {self._nombre} | "
            f"Especialista: {self.especialista}"
        )