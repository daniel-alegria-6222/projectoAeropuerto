
from fechahora import Fecha, Hora
from vuelo import Vuelo

class Organizador:
    def __init__ ( self ):
        self.vuelos = list()
        self.atencionDe6AvionesCada30Minutos = "?"

    def showVuelos ( fecha = Fecha.today() ):
        pass

    def getInfoVuelo ( user ):
        pass

    def setVueloAttr ( vuelo: Vuelo, attribute, value ):
        if attribute in vars(vuelo):
            setattr(vuelo, attribute, value)


    def incluir ( vuelo: Vuelo ):
        pass

    def modificar ( vuelo: Vuelo ):
        pass

    def excluir ( vuelo: Vuelo ):
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
