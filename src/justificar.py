import silabar
import os


def justificar_linea(linea, ancho):
    palabras = linea.split()
    long_palabras = 0
    for palabra in palabras:
        long_palabras = long_palabras + len(palabra)
    espacios = ancho - long_palabras - 1  # calcular el espacio a rellenar
    if len(palabras) == 1:
        palabras[0] = palabras[0] + ' ' * espacios
    else:
        while espacios > 0:
            for i in range(len(palabras) - 1):
                palabras[i] = palabras[i] + ' '
                espacios = espacios - 1
                if espacios == 0:
                    break
    return ''.join(palabras)


def justificar_texto(texto, ancho):
    texto_justificado = []  # Una lista que luego se une con \n
    lineas = texto.splitlines()
    for linea in lineas:
        if linea != '':
            palabras = linea.split()
            linea_actual = ''
            lista_silabas = []
            for palabra in palabras:
                silabas = silabar.obtener_silabas(palabra)
                silabas = silabas.split('-')
                if len(lista_silabas) == 0:
                    lista_silabas = lista_silabas + silabas
                else:
                    lista_silabas.append(' ')
                    lista_silabas = lista_silabas + silabas
            linea_actual = linea_actual + lista_silabas[0]
            contador = 1
            for silaba in lista_silabas[1:-1]:
                if silaba == ' ' and linea_actual == '':  # evitar espacios al inicio de la linea
                    linea_actual = linea_actual
                elif len(linea_actual) + len(silaba) + 1 < ancho:
                    linea_actual = linea_actual + silaba
                elif len(linea_actual) + len(silaba) + 1 == ancho and silaba == ' ':  # justo ha terminado la palabra
                    texto_justificado.append(linea_actual.ljust(ancho-1))
                    linea_actual = ''
                elif len(linea_actual) + len(silaba) + 1 == ancho and silaba != ' ':
                    if lista_silabas[contador + 1] == ' ' and lista_silabas[contador - 1] == ' ':  # monosílabas
                        linea_actual = linea_actual + silaba
                        texto_justificado.append(linea_actual.ljust(ancho-1))
                        linea_actual = ''
                    elif lista_silabas[contador + 1] == ' ' and not linea.endswith(silaba):  # final de una palabra
                        linea_actual = linea_actual + silaba
                        texto_justificado.append(linea_actual.ljust(ancho-1))
                        linea_actual = ''
                    elif lista_silabas[contador - 1] == ' ':  # principio de otra palabra
                        texto_justificado.append(linea_actual[:-1].ljust(ancho-1))
                        linea_actual = silaba
                    else:
                        linea_actual = linea_actual + '-'
                        texto_justificado.append(linea_actual.ljust(ancho-1))
                        linea_actual = silaba
                else:  # es mayor que el ancho
                    if lista_silabas[contador + 1] == ' ' and lista_silabas[contador - 1] == ' ':  # monosílabas
                        texto_justificado.append(justificar_linea(linea_actual[:-1], ancho))
                        linea_actual = silaba
                    elif lista_silabas[contador + 1] == ' ':  # final de una palabra
                        linea_actual = linea_actual + '-'
                        texto_justificado.append(justificar_linea(linea_actual, ancho))
                        linea_actual = silaba
                    elif lista_silabas[contador - 1] == ' ':  # principio de una palabra
                        texto_justificado.append(justificar_linea(linea_actual[:-1], ancho))
                        linea_actual = silaba
                    else:
                        linea_actual = linea_actual + '-'
                        texto_justificado.append(justificar_linea(linea_actual, ancho))
                        linea_actual = silaba
                contador = contador + 1
            if len(lista_silabas[-1]) + len(linea_actual) <= ancho - 1:
                linea_actual = linea_actual + lista_silabas[-1]
                texto_justificado.append(linea_actual.ljust(ancho-1))
            else:
                if lista_silabas[-1] == ' ':
                    texto_justificado.append(linea_actual.ljust(ancho-1))
                    linea_actual = lista_silabas[-1]
                    texto_justificado.append(linea_actual.ljust(ancho-1))
                else:
                    linea_actual = linea_actual + '-'
                    texto_justificado.append(linea_actual.ljust(ancho-1))
                    linea_actual = lista_silabas[-1]
                    texto_justificado.append(linea_actual.ljust(ancho-1))
        else:
            texto_justificado.append(linea)
    return '\n'.join(texto_justificado)


'''
        print("Opción 1 -> A partir de un archivo (.txt) e imprimir por pantalla")
        print("Opción 2 -> A partir de un archivo (.txt) y pasarlo a otro archivo (.txt)")
        print("Opción 3 -> Introducir en la terminal e imprimir por pantalla")
        print("Opción 4 -> Introducir en la terminal y pasarlo a otro archivo (.txt)")
'''


def interprete_justificar(opcion):
    if opcion == 1:
        nombre_archivo = input("¿Cuál es el nombre del archivo que desea justificar? (sin extensión): ")
        nombre_archivo = nombre_archivo + '.txt'
        ancho = input("¿Qué ancho debe tener cada línea? ")
        try:
            ancho = int(ancho)
        except ValueError:
            print("El valor debe ser un entero de entre las opciones")
        else:
            if not os.path.isfile(nombre_archivo):
                print('El archivo no se encuentra en su directorio.')
            else:
                with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read()
                    justificado = justificar_texto(contenido, ancho)
                print(justificado)
        finally:
            return
    elif opcion == 2:
        nombre_archivo = input("¿Cuál es el nombre del archivo que desea justificar? (sin extensión): ")
        nombre_archivo = nombre_archivo + '.txt'
        ancho = input("¿Qué ancho debe tener cada línea? ")
        try:
            ancho = int(ancho)
        except ValueError:
            print("El valor debe ser un entero de entre las opciones")
        else:
            if not os.path.isfile(nombre_archivo):
                print('El archivo no se encuentra en su directorio.')
            else:
                with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read()
                    justificado = justificar_texto(contenido, ancho)
                nombre_devuelto = input("¿Con qué nombre quiere que se guarde el archivo creado? (sin extensión): ")
                nombre_devuelto = nombre_devuelto + '.txt'
                with open(nombre_devuelto, 'w') as archivo:
                    archivo.write(justificado)
                print(f'Guardando como {nombre_devuelto} ...')
        finally:
            return
    elif opcion == 3:
        texto = input("Introduzca el texto a justificar: ")
        ancho = input("¿Qué ancho debe tener cada línea? ")
        try:
            ancho = int(ancho)
        except ValueError:
            print("El valor debe ser un entero de entre las opciones")
        else:
            justificado = justificar_texto(texto, ancho)
            print(justificado)
        finally:
            return
    elif opcion == 4:
        texto = input("Introduzca el texto a justificar: ")
        ancho = input("¿Qué ancho debe tener cada línea? ")
        try:
            ancho = int(ancho)
        except ValueError:
            print("El valor debe ser un entero de entre las opciones")
        else:
            justificado = justificar_texto(texto, ancho)
            nombre_devuelto = input("¿Con qué nombre quiere que se guarde el archivo creado? (sin extensión): ")
            nombre_devuelto = nombre_devuelto + '.txt'
            with open(nombre_devuelto, 'w') as archivo:
                archivo.write(justificado)
                print(f'Guardando como {nombre_devuelto} ...')
        finally:
            return
    else:
        print("La opción indicada no es válida.")
