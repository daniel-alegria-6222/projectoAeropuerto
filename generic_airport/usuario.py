from generic_airport.fechahora import Fecha

class Usuario:
    def __init__ ( self, nombreCompleto, telefono, email, dni, fechaNacimiento ):
        self.nombreCompleto  = nombreCompleto
        self.telefono        = telefono
        self.email           = email
        self.dni             = str(dni)
        self.fechaNacimiento = fechaNacimiento
        # lista de codigos
        self.viajes = list()

    def __eq__ ( self, otherPassenger):
        return self.dni == otherPassenger.dni

    def addViaje ( self, nroVuelo ):
        if nroVuelo not in self.viajes:
            self.viajes.append( nroVuelo )
            return True
        return False


