from coordenadas import * 
import csv
from collections import namedtuple

CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, Coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci')

def leer_centros(archivo):
    lista_centros = []
    with open(archivo, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for nombre, localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci in lector:
            nombre = str(nombre)
            localidad = str(localidad)
            latitud = float(latitud)
            longitud = float(longitud)
            estado = str(estado)
            num_camas = int(num_camas)
            acceso_minusvalidos = bool(acceso_minusvalidos)
            tiene_uci = bool(tiene_uci)
            tupla = CentroSanitario(nombre, localidad, Coordenadas(latitud, longitud), estado, num_camas, acceso_minusvalidos, tiene_uci)
            lista_centros.append(tupla) 
            
    return lista_centros



def calcular_total_camas_centros_accesibles(lista_centros):
    total_camas_accesibles = 0
    for e in lista_centros:
        if e.tiene_uci == True:
            total_camas_accesibles = total_camas_accesibles + e.num_camas
    return total_camas_accesibles


def obtener_centros_con_uci_cercanos_a(lista_centros, tupla_punto, umbral):
    centros_dentro_umbral = []
    for e in lista_centros:
        if calcular_distancia(e.Coordenadas, tupla_punto) <= umbral:
            tupla = (e.nombre, e.localidad, e.Coordenadas)
            centros_dentro_umbral.append(tupla)
    return centros_dentro_umbral

lista_centros = leer_centros("./data/centrosSanitarios.csv")

print(lista_centros)

