import regex as re
import silabar
import entonar
import diccionario
import rimas
import justificar


dic = diccionario.archivo_a_diccionario_general()
print(dic)
asonantes = diccionario.archivo_a_diccionario_rimas_aso()
consonantes = diccionario.archivo_a_diccionario_rimas_cons()

# Usamos expresiones regulares para ver si lo introducido por el usuario es una palabra
er_palbra = r'(?i)^[a-záéíóúüñ]+$'
patron_palabra = re.compile(er_palbra)  # Si se pone aquí lo compila una única vez al ejecutar el programa


def interprete(num):
    if num == 1:
        palabras = input("Introduce una o varias palabras separadas por espacios (presione ENTER al terminar): ")
        lista_palabras = palabras.split()
        if len(lista_palabras) == 0:
            print("No se ha introducido ninguna palabra.")
            return
        else:
            for palabra in lista_palabras:
                if patron_palabra.match(palabra):
                    palabra = palabra.lower()
                    if palabra in dic["Palabra"]:
                        indice = dic["Palabra"].index(palabra)
                        silabas = dic["Sílabas"][indice]
                    else:
                        silabas = silabar.obtener_silabas(palabra)
                        resultado = entonar.entonacion(silabas)
                        term_cons = rimas.terminacion_consonante(palabra)
                        term_aso = rimas.terminacion_asonante(palabra)
                        diccionario.insertar_diccionario_general(dic, palabra, silabas, resultado[:2], term_cons, term_aso)
                        diccionario.insertar_diccionario_rimas(consonantes, palabra, term_cons)
                        diccionario.insertar_diccionario_rimas(asonantes, palabra, term_aso)
                    print(f"Sílabas de {palabra}:", silabas)
                else:
                    print(f'La palabra "{palabra}" no es válida.')
    elif num == 2:
        palabras = input("Introduce una o varias palabras separadas por espacios: ")
        lista_palabras = palabras.split()
        if len(lista_palabras) == 0:
            print("No se ha introducido ninguna palabra.")
            return
        else:
            for palabra in lista_palabras:
                if patron_palabra.match(palabra):
                    palabra = palabra.lower()
                    if palabra in dic["Palabra"]:
                        indice = dic["Palabra"].index(palabra)
                        resultado = dic["Entonación"][indice]
                    else:
                        silabas = silabar.obtener_silabas(palabra)
                        resultado = entonar.entonacion(silabas)
                        term_cons = rimas.terminacion_consonante(palabra)
                        term_aso = rimas.terminacion_asonante(palabra)
                        diccionario.insertar_diccionario_general(dic, palabra, silabas, resultado[:2], term_cons, term_aso)
                        diccionario.insertar_diccionario_rimas(consonantes, palabra, term_cons)
                        diccionario.insertar_diccionario_rimas(asonantes, palabra, term_aso)
                    print(resultado[:2])
                else:
                    print(f'La palabra "{palabra}" no es válida')
    elif num == 3:
        palabras = input("Introduce palabras separadas por espacios para buscar rimas: ")
        lista_palabras = palabras.split()
        if len(lista_palabras) == 0:
            print("No se ha introducido ninguna palabra.")
            return
        else:
            for palabra in lista_palabras:
                if patron_palabra.match(palabra):
                    palabra = palabra.lower()
                    term_cons = rimas.terminacion_consonante(palabra)
                    term_aso = rimas.terminacion_asonante(palabra)
                    if palabra not in dic["Palabra"]:
                        diccionario.insertar_diccionario_general(dic, palabra, silabar.obtener_silabas(palabra), entonar.entonacion(palabra)[:2], term_cons, term_aso)
                        diccionario.insertar_diccionario_rimas(consonantes, palabra, term_cons)
                        diccionario.insertar_diccionario_rimas(asonantes, palabra, term_aso)
                    print(f'Las palabras en diccionario con rima consonante de {palabra} son: ', consonantes[term_cons])
                    print(f'Las palabras en diccionario con rima asonante de {palabra} son: ', asonantes[term_aso])
                else:
                    print(f'La palabra "{palabra}" no es válida')
    elif num == 4:
        print("Menú de opciones para justificar:")
        print("Opción 1 -> A partir de un archivo (.txt) e imprimir por pantalla")
        print("Opción 2 -> A partir de un archivo (.txt) y pasarlo a otro archivo (.txt)")
        print("Opción 3 -> Introducir en la terminal e imprimir por pantalla")
        print("Opción 4 -> Introducir en la terminal y pasarlo a otro archivo (.txt)")
        valor = input("Introduzca una opción (solo el número): ")
        try:
            valor = int(valor)
        except ValueError:
            print("El valor debe ser un entero de entre las opciones")
        else:
            justificar.interprete_justificar(valor)
        finally:
            return

    elif num == 5:
        diccionario.diccionario_a_archivo_general(dic)
        diccionario.diccionario_a_archivo_rima_aso(asonantes)
        diccionario.diccionario_a_archivo_rima_cons(consonantes)
        exit()
    else:
        print("Debe ser un número natural de entre las opciones (sin espacios ni caracteres especiales)")


if __name__ == "__main__":

    while True:
        print("Menú de opciones:")
        print("Opción 1 -> Silabear palabras")
        print("Opción 2 -> Clasificar palabras")
        print("Opción 3 -> Rimas de palabras")
        print("Opción 4 -> Justificar texto")
        print("Opción 5 -> Finalizar")
        opcion = input("Introduzca una opción (solo el número): ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("El valor debe ser un entero de entre las opciones")
        else:
            interprete(opcion)
