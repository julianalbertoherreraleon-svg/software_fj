from modelos.excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado == "Confirmada":
            raise ReservaError(
                "La reserva ya fue confirmada"
            )

        self.estado = "Confirmada"

    def cancelar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "La reserva ya fue cancelada"
            )

        self.estado = "Cancelada"

    def procesar_reserva(self):

        try:

            costo = self.servicio.calcular_costo(
                self.duracion
            )

            self.confirmar()

            return (
                f"Reserva procesada correctamente\n"
                f"{self.cliente.mostrar_informacion()}\n"
                f"{self.servicio.mostrar_informacion()}\n"
                f"Costo total: ${costo}\n"
                f"Estado: {self.estado}"
            )

        except Exception as e:

            raise ReservaError(
                f"Error procesando reserva: {e}"
            )