from coordenadas import *
from test_centros import *


def test_calcular_distancia():
    distancia = calcular_distancia((36.135051666002795, -5.843455923196172),(36.87946545201232, -5.402516807153386))

    print(distancia)



def test_calcular_media_coordenanas():
    media_coordenadas = calcular_media_coordenadas(lista_coordenadas)
    print(media_coordenadas)


test_calcular_media_coordenanas()