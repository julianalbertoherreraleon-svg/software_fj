from modelos.cliente import Cliente
from modelos.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from modelos.reserva import Reserva
from modelos.excepciones import (
    ClienteError,
    ServicioError,
    ReservaError
)


def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        archivo.write(mensaje + "\n")


def ejecutar_sistema():

    operaciones = []

    try:

        cliente1 = Cliente(
            "Julian Leon",
            "julian@gmail.com",
            "3001234567"
        )

        operaciones.append(cliente1)

    except ClienteError as e:

        registrar_log(str(e))

    try:

        cliente2 = Cliente(
            "",
            "correo_invalido",
            "abc123"
        )

        operaciones.append(cliente2)

    except ClienteError as e:

        registrar_log(str(e))

    try:

        sala = ReservaSala(
            "Sala Premium",
            100,
            20
        )

        equipo = AlquilerEquipo(
            "Computador Gamer",
            80,
            "PC"
        )

        asesoria = AsesoriaEspecializada(
            "Python Avanzado",
            150,
            "Carlos Perez"
        )

        operaciones.extend([sala, equipo, asesoria])

    except ServicioError as e:

        registrar_log(str(e))

    try:

        servicio_error = ReservaSala(
            "Sala Error",
            -50,
            10
        )

        operaciones.append(servicio_error)

    except ServicioError as e:

        registrar_log(str(e))

    try:

        reserva1 = Reserva(
            cliente1,
            sala,
            3
        )

        print(reserva1.procesar_reserva())

    except ReservaError as e:

        registrar_log(str(e))

    try:

        reserva2 = Reserva(
            cliente1,
            equipo,
            2
        )

        print(reserva2.procesar_reserva())

    except ReservaError as e:

        registrar_log(str(e))

    try:

        reserva3 = Reserva(
            cliente1,
            asesoria,
            4
        )

        print(reserva3.procesar_reserva())

    except ReservaError as e:

        registrar_log(str(e))

    try:

        reserva1.confirmar()

    except ReservaError as e:

        registrar_log(str(e))

    try:

        reserva1.cancelar()

        reserva1.cancelar()

    except ReservaError as e:

        registrar_log(str(e))

    print("\nSistema ejecutado correctamente")


ejecutar_sistema()