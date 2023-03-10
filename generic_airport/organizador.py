
from generic_airport.fechahora import Fecha
from generic_airport.vuelo import Vuelo, Avion
from generic_airport.usuario import Usuario

class Organizador:
    def __init__ ( self ):
        self.vuelos = list()
        self.usuarios = list()
        self.aviones = list()

    def guardarDatos ( self, filename = "dataout.txt" ):
        pass

#######
    def getViajesDeUsuario ( self, user ):
        rpta = list()
        for nroVuelo in user.viajes:
            rpta.append( self.getVueloByNro(nroVuelo) )
        return rpta

    def getPasajerosDeVuelo ( self, vuelo ):
        rpta = list()
        for dni in vuelo.pasajeros:
            rpta.append( self.getUsuarioByNro(dni) )
        return rpta

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

    def getAvionByNro ( self, codigo ):
        for avion in self.aviones:
            if str(avion.codigo) == str(codigo):
                return avion
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
        i = 0
        while i < len(self.vuelos):
            if self.vuelos[i] == vuelo:
                del self.vuelos[i]
                return True
            i += 1
        return False

    ### USUARIOS
    def incluirUsuario ( self, user :Usuario ):
        if user not in self.usuarios:
            self.usuarios.append(user)
            return True
        return False

    def updateUsuario ( self, ant_user, user ):
        i = 0
        while i < len(self.usuarios):
            if self.usuarios[i] == ant_user :
                self.usuarios[i] = user
                return True
            i += 1
        return False

    def deleteUsuario ( self, user :Usuario ):
        i = 0
        while i < len(self.usuarios):
            if self.usuarios[i] == user:
                del self.usuarios[i]
                return True
            i += 1
        return False

    ### AVIONES
    def incluirAvion ( self, avion :Avion ):
        if avion not in self.aviones:
            self.aviones.append(avion)
            return True
        return False

    def updateAvion ( self, ant_avion, avion ):
        i = 0
        while i < len(self.aviones):
            if self.aviones[i] == ant_avion :
                self.aviones[i] = avion
                return True
            i += 1
        return False

    def deleteAvion ( self, avion :Avion ):
        i = 0
        while i < len(self.aviones):
            if self.aviones[i] == avion:
                del self.aviones[i]
                return True
            i += 1
        return False


    ### Operaciones gerenciales
    def nroVuelosPorMes ( self ):
        rpta = { key:0 for key in Fecha.MONTHS }
        for vuelo in self.vuelos:
            rpta[vuelo.fecha.getNamedMonth()] += 1
        return rpta

    def calcularGanacia ( self ):
        return len(self.vuelos) * 15000

    def advertencia ( self ):
        pass


    ### lista de pasajeros en un vuelo
    def enumerarPasajerosEnVuelo ( self, vuelo ):
        pass
