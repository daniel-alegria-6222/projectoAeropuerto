
from fechahora import Fecha, Hora

class Avion:
    def __init__ ( self ):
        self.autonomiaDeVuelo_KM
        self.altura
        self.longitudAla
        self.capacidad_Toneladas
        self.pasajeros = list()

class Vuelo:
    ESTADOS = ["confirmado", "cancelado", "retrasado"]

    def __init__ ( self, nroVuelo, aerolinea,
                   avion, fecha, hora,
                   estado, destino, origen ):

        self.nroVuelo  = nroVuelo
        self.aerolinea = aerolinea
        self.avion     = avion
        self.fecha     = fecha
        self.hora      = hora
        self.estado    = estado
        self.destino   = destino
        self.origen    = origen
