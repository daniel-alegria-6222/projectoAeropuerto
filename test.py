import generic_airport as ga
org = ga.Organizador()
a = ga.Vuelo(666, "latam", "perla", ga.Fecha.today(), ga.Hora(11,22), "confirmado", "usa", "peru" )

org.incluirVuelo(a)

v = org.getVueloByNro(666)
print(v)

b = ga.Vuelo(777, "noase", "nosae", ga.Fecha.today(), ga.Hora(11,22), "confirmado", "usa", "peru" )
print(org.updateVuelo(666, b))

print(org.vuelos[0].nroVuelo)
print(org.vuelos[0].aerolinea)
print(org.vuelos[0].avion)
print(org.vuelos[0].fecha)
print(org.vuelos[0].hora)
print(org.vuelos[0].estado)
print(org.vuelos[0].destino)
print(org.vuelos[0].origen)

print("------")
v = org.getVueloByNro(777)
print(v)
print(org.updateVuelo(666, a))
print(org.vuelos[0].nroVuelo)
print(org.vuelos[0].aerolinea)
print(org.vuelos[0].avion)
print(org.vuelos[0].fecha)
print(org.vuelos[0].hora)
print(org.vuelos[0].estado)
print(org.vuelos[0].destino)
print(org.vuelos[0].origen)
