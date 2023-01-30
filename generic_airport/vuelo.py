
from generic_airport.fechahora import Fecha, Hora

class Avion:
    def __init__ ( self,
            codigo, autonomiaDeVueloKM, altura, longitudAla, capacidadToneladas ):
        self.codigo = str(codigo)
        self.autonomiaDeVueloKM = autonomiaDeVueloKM
        self.altura = altura
        self.longitudAla = longitudAla
        self.capacidadToneladas = capacidadToneladas

    def __eq__ ( self, other ):
        return self.codigo == other.codigo


class Vuelo:
    ESTADOS = ["confirmado", "cancelado", "retrasado"]

    def __init__ ( self, nroVuelo, aerolinea,
                   avion, fecha, hora,
                   estado, destino, origen, pasajeros=[]):

        self.nroVuelo  = str(nroVuelo)
        self.aerolinea = aerolinea
        self.avion     = avion # solo es el codigo del avion, no el objeto
        self.fecha     = fecha
        self.hora      = hora
        self.estado    = estado
        self.destino   = destino
        self.origen    = origen
        # lista de dni's
        self.pasajeros = pasajeros

    def __eq__ ( self, other ):
        return self.nroVuelo == other.nroVuelo

    def addPasajero( self, dni ):
        if dni not in self.pasajeros:
            self.pasajeros.append( dni )
            return True
        return False

