
from generic_airport.fechahora import Fecha, Hora
from generic_airport.vuelo import Vuelo

class Organizador:
    def __init__ ( self ):
        self.vuelos = list()
        self.atencionDe6AvionesCada30Minutos = "?"


    def showVuelosEnFecha ( fecha = Fecha.today() ):
        pass

    def getInfoVuelo ( user ):
        pass

    def setVueloAttr ( vuelo: Vuelo, attribute, value ):
        if attribute in vars(vuelo):
            setattr(vuelo, attribute, value)


    def incluirVuelo ( vuelo: Vuelo ):
        pass

    def modificarVuelo ( vuelo: Vuelo ):
        pass

    def excluirVuelo ( vuelo: Vuelo ):
        pass


    def nroVuelosPorMes ( self ):
        pass

    def calcularGanacia ( self ):
        # for vuelo in self.vuelos:
        pass

    def advertencia ( self ):
        pass

    def enumerarPasajeros ( self, vuelo: Vuelo ):
        pass
