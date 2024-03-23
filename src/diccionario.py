import os
import csv
from itertools import zip_longest


# dic = {"Palabra": [], "Sílabas": [], "Entonación": [], "Rima_asonante": [], "Rima_consonante": []}
def insertar_diccionario_general(diccionario, palabra, silabas, entonacion, rimas_cons, rimas_as):
    diccionario["Palabra"].append(palabra)
    diccionario["Sílabas"].append(silabas)
    diccionario["Entonación"].append(entonacion)
    diccionario["Rima_asonante"].append(rimas_as)
    diccionario["Rima_consonante"].append(rimas_cons)


def insertar_diccionario_rimas(diccionario, palabra, terminacion):
    if terminacion in diccionario.keys():
        if palabra not in diccionario[terminacion]:
            diccionario[terminacion].append(palabra)
    else:
        diccionario[terminacion] = []
        diccionario[terminacion].append(palabra)


def diccionario_a_archivo_general(diccionario):
    print('Guardando archivo como "palabras.csv"...')
    claves = diccionario.keys()
    filas = zip_longest(*diccionario.values(), fillvalue='')
    # Combina los iterables de diferentes longitudes y los alinea juntos, en este caso sin rellenar
    # El * sirve para desempaquetar los valores del diccionario
    with open('palabras.csv', 'w', newline='') as archivo:
        escribir = csv.writer(archivo, delimiter=';')
        escribir.writerow(claves)   # Pone las claves como título
        escribir.writerows(filas)
    return


def diccionario_a_archivo_rima_cons(diccionario):
    print('Guardando archivo como "rimasconsonantes.csv"...')
    claves = diccionario.keys()
    filas = zip_longest(*diccionario.values(), fillvalue='')
    # Combina los iterables de diferentes longitudes y los alinea juntos, en este caso sin rellenar
    # El * sirve para desempaquetar los valores del diccionario
    with open('rimasconsonantes.csv', 'w', newline='') as archivo:
        escribir = csv.writer(archivo, delimiter=';')
        escribir.writerow(claves)   # Pone las claves como título
        escribir.writerows(filas)
    return


def diccionario_a_archivo_rima_aso(diccionario):
    print('Guardando archivo como "rimasasonantes.csv"...')
    claves = diccionario.keys()
    filas = zip_longest(*diccionario.values(), fillvalue='')
    # Combina los iterables de diferentes longitudes y los alinea juntos, en este caso sin rellenar
    # El * sirve para desempaquetar los valores del diccionario
    with open('rimasasonantes.csv', 'w', newline='') as archivo:
        escribir = csv.writer(archivo, delimiter=';')
        escribir.writerow(claves)   # Pone las claves como título
        escribir.writerows(filas)
    return


def archivo_a_diccionario_general():
    if os.path.isfile('palabras.csv'):
        dic = {}
        with open('palabras.csv', 'r', newline='') as archivo:
            leer = csv.reader(archivo, delimiter=';')
            claves = next(leer)  # Lee los encabezados
            for fila in leer:
                for posicion, valor in enumerate(fila):
                    clave = claves[posicion]
                    if clave not in dic:
                        dic[clave] = []
                    dic[clave].append(valor)
    else:
        dic = {"Palabra": [], "Sílabas": [], "Entonación": [], "Rima_asonante": [], "Rima_consonante": []}
    return dic


def archivo_a_diccionario_rimas_cons():
    if os.path.isfile('rimasconsonantes.csv'):
        dic = {}
        with open('rimasconsonantes.csv', 'r', newline='') as archivo:
            leer = csv.reader(archivo, delimiter=';')
            claves = next(leer)  # Lee los encabezados
            for fila in leer:
                for posicion, valor in enumerate(fila):
                    clave = claves[posicion]
                    if clave not in dic:
                        dic[clave] = []
                    dic[clave].append(valor)
    else:
        dic = {}
    return dic


def archivo_a_diccionario_rimas_aso():
    if os.path.isfile('rimasasonantes.csv'):
        dic = {}
        with open('rimasasonantes.csv', 'r', newline='') as archivo:
            leer = csv.reader(archivo, delimiter=';')
            claves = next(leer)  # Lee los encabezados
            for fila in leer:
                for posicion, valor in enumerate(fila):
                    clave = claves[posicion]
                    if clave not in dic:
                        dic[clave] = []
                    dic[clave].append(valor)
    else:
        dic = {}
    return dic
