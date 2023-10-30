
from math import dist
from collections import namedtuple
from centros import *
from coordenadas import *

Coordenadas = namedtuple("Coordenadas", "latitud, longitud")

def calcular_distancia(coordenada1, coordenada2):
    distancia = float(dist(coordenada1, coordenada2))

    return distancia


def calcular_media_coordenadas(lista_coordenadas):
    suma_latitud = 0
    la = 0

    suma_longitud = 0
    lo = 0

    for e in lista_coordenadas:
        suma_latitud = suma_latitud + e.latitud
        la = la + 1

        suma_longitud = suma_longitud + e.longitud
        lo = lo +1

        media_latitud = suma_latitud/la
        media_longitud = suma_longitud/lo

        media_coordenadas = Coordenadas(media_latitud, media_longitud)


    return media_coordenadas







