from generic_airport.fechahora import Fecha

class Pasajero:
    def __init__ ( self, nombreCompleto, telefono, email, dni, fechaNacimiento ):
        self.nombreCompleto  = nombreCompleto
        self.telefono        = telefono
        self.email           = email
        self.dni             = dni
        self.fechaNacimiento = fechaNacimiento

    def __eq__ ( self, otherPassenger):
        return self.dni == otherPassenger.dni


