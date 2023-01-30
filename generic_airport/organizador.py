
from generic_airport.fechahora import Fecha, Hora
from generic_airport.vuelo import Vuelo, Avion
from generic_airport.usuario import Usuario

class Organizador:
    def __init__ ( self ):
        self.vuelos = list()
        self.usuarios = list()
        self.aviones = list()
        self.atencionDe6AvionesCada30Minutos = "?"

    def guardarDatos ( self, filename = "dataout.txt" ):
        pass

#######
    def getVuelosByFecha ( self, fecha = Fecha.today() ):
        rpta = list()
        for vuelo in self.vuelos:
            if vuelo.fecha == fecha:
                rpta.append(vuelo)
        return rpta

    def getVueloByNro ( self, nroVuelo ):
        for vuelo in self.vuelos:
            if str(vuelo.nroVuelo) == str(nroVuelo):
                return vuelo
        return None

    def getUsuarioByNro ( self, dni ):
        for user in self.usuarios:
            if str(user.dni) == str(dni):
                return user
        return None
#######


    ### VUELOS
    def incluirVuelo ( self, vuelo :Vuelo ):
        if vuelo not in self.vuelos:
            self.vuelos.append(vuelo)
            return True
        return False

    def updateVuelo ( self, ant_vuelo, vuelo):
        i = 0
        while i < len(self.vuelos):
            if self.vuelos[i] == ant_vuelo :
                self.vuelos[i] = vuelo
                return True
            i += 1
        return False

    def deleteVuelo ( self, vuelo :Vuelo ):
        pass

    ### USUARIOS
    def incluirUsuario ( self, user :Usuario ):
        if user not in self.usuarios:
            self.usuarios.append(user)
            return True
        return False

    def updateUsuario ( self, ant_user, user ):
        pass

    def deleteUsuario ( self, user :Usuario ):
        pass

    ### AVIONES
    def incluirAvion ( self, avion :Avion ):
        if avion not in self.aviones:
            self.aviones.append(avion)
            return True
        return False

    def updateAvion ( self, ant_avion, avion ):
        pass

    def deleteAvion ( self, avion :Avion ):
        pass


    ### Operaciones gerenciales
    def nroVuelosPorMes ( self ):
        pass

    def calcularGanacia ( self ):
        # for vuelo in self.vuelos:
        pass

    def advertencia ( self ):
        pass

    def enumerarPasajerosEnVuelo ( self):
        pass
