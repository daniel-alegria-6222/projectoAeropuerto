
from generic_airport.fechahora import Fecha, Hora
from generic_airport.usuario import Usuario

class Avion:
    def __init__ ( self,
            codigo, autonomiaDeVueloKM, altura, longitudAla, capacidadToneladas ):
        self.codigo = codigo
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
                   estado, destino, origen, pasajeros=None):

        self.nroVuelo  = str(nroVuelo)
        self.aerolinea = aerolinea
        self.avion     = avion
        self.fecha     = fecha
        self.hora      = hora
        self.estado    = estado
        self.destino   = destino
        self.origen    = origen
        # lista de dni's
        self.pasajeros = list()

    def __eq__ ( self, other ):
        return self.nroVuelo == other.nroVuelo

    def incluirPasajero( dni ):
        self.pasajeros.append( dni )

