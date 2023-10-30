from centros import *

def test_leer_centros():
    lista_centros = leer_centros("./data/centrosSanitarios.csv")
    for e in lista_centros:
        print(e)
        

def test_calcular_total_camas_centros_accesibles():
    lista_centros = leer_centros("./data/centrosSanitarios.csv")
    print(calcular_total_camas_centros_accesibles(lista_centros))





def test_obtener_centros_con_uci_cercanos_a():
    centros_dentro_umbral = obtener_centros_con_uci_cercanos_a(lista_centros, (36,-5), 5)
    for e in centros_dentro_umbral:
        print(e)



test_obtener_centros_con_uci_cercanos_a()


