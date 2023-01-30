from generic_airport.fechahora import Fecha

class Usuario:
    def __init__ ( self, nombreCompleto, telefono, email, dni, fechaNacimiento, viajes=[] ):
        self.nombreCompleto  = nombreCompleto
        self.telefono        = telefono
        self.email           = email
        self.dni             = str(dni)
        self.fechaNacimiento = fechaNacimiento
        # lista de nroVuelo
        self.viajes = viajes

    def __eq__ ( self, user):
        return self.dni == user.dni

    def addViaje ( self, nroVuelo ):
        if nroVuelo not in self.viajes:
            self.viajes.append( nroVuelo )
            return True
        return False


