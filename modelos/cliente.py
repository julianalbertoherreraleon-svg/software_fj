from modelos.entidad import Entidad
from modelos.excepciones import ClienteError


class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        super().__init__(nombre)

        self._correo = correo
        self._telefono = telefono

        self.validar_datos()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):

        if "@" not in valor:
            raise ClienteError("Correo electrónico inválido")

        self._correo = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):

        if not valor.isdigit():
            raise ClienteError("El teléfono solo debe contener números")

        self._telefono = valor

    def validar_datos(self):

        if not self._nombre.strip():
            raise ClienteError("El nombre del cliente está vacío")

        if "@" not in self._correo:
            raise ClienteError("Correo inválido")

        if not self._telefono.isdigit():
            raise ClienteError("Teléfono inválido")

    def mostrar_informacion(self):

        return (
            f"Cliente: {self._nombre} | "
            f"Correo: {self._correo} | "
            f"Teléfono: {self._telefono}"
        )