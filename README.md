
# ALF - Silabeador Regex Project

La aplicación a realizar consiste fundamentalmente en un silabeador, es decir, un programa capaz de separar en sílabas las palabras de un texto en castellano. Usando dicha información, la aplicación podrá realizar otras tareas como poner guiones ortográficos para dividir una palabra al final de una frase cuando se formatea un texto, o encontrar palabras que rimen. 

La nota de este proyecto fue de un 9.9


## Autoría

- [@evaapinaa](https://www.github.com/evaapinaa)


![Logo](https://www.um.es/documents/1073494/42130150/LogosimboloUMU-positivo.png/e1f004bd-ed22-23dd-682f-ab3f1f39b435?t=1693480807647&download=true)


## Acknowledgements

 - [Apéndice](https://github.com/evaapinaa/ALF-Regex-Project?tab=readme-ov-file#ap%C3%A9ndice)
 - [Manual de usuario](https://github.com/evaapinaa/ALF-Regex-Project?tab=readme-ov-file#manual-de-usuario)
 - [main.py](https://github.com/evaapinaa/ALF-Regex-Project?tab=readme-ov-file#main)
 - [diccionario.py](https://github.com/evaapinaa/ALF-Regex-Project?tab=readme-ov-file#diccionario)
 - [silabar.py](https://github.com/evaapinaa/ALF-Regex-Project?tab=readme-ov-file#silabear)
 - [entonar.py](https://github.com/evaapinaa/ALF-Regex-Project?tab=readme-ov-file#entonaci%C3%B3n)
 - [rimas.py](https://github.com/evaapinaa/ALF-Regex-Project?tab=readme-ov-file#rimas)
 - [justificar.py](https://github.com/evaapinaa/ALF-Regex-Project?tab=readme-ov-file#justificar)

## Apéndice

Para la realización de este proyecto, se ha optado por la creación de diversos módulos. Cada uno ha sido nombrado con su funcionalidad, facilitando así la legibilidad y organización del código. Los módulos son los siguientes: 
- main.py: punto de entrada principal del proyecto. También contiene el intérprete de las opciones que llama a las distintas funciones de los otros módulos 
- silabar.py: se implementan las funciones necesarias para devolver un string con las distintas sílabas de una palabra
- entonar.py: implementación para la entonación de las palabras
- diccionario.py: implementación para la gestión de los tres diccionarios y pasarlos a un archivo CSV a la vez que leer el contenido de este para formar los diccionarios al comienzo de la ejecución del programa
- rimas.py: implementación para devolver las terminaciones de las palabras 
- justificar.py: implementación para justificar un texto dada una anchura y el intérprete de opciones ofrecidas al usuario


## Manual de usuario

Cada opción dada al usuario se asocia a un número que será el que tendrá que 
introducir

```txt
Menú de opciones:
Opción 1 -> Silabear palabras
Opción 2 -> Clasificar palabras
Opción 3 -> Rimas de palabras
Opción 4 -> Justificar texto
Opción 5 -> Finalizar
Introduzca una opción (solo el número):

```

- Opción 1: Devuelve las sílabas de tantas palabras como el usuario desee, siempre que las ingrese separadas por espacios y se presione la tecla ENTER al finalizar la inserción.
- Opción 2: Devuelve la entonación de la palabra y el tipo de tantas palabras como el usuario desee, siempre que se cumplan las mismas condiciones que en la primera opción
- Opción 3: Dadas tantas palabras como el usuario desee, introducidas de la misma forma que en las opciones anteriores, devuelve las palabras que se encuentren en el diccionario del programa, formado por las palabras que ingresa el usuario, que tengan rima consonante y rima asonante con cada una de las palabras introducidas
- Opción 4: Se muestra el siguiente menú:

```txt
Menú de opciones para justificar:
Opción 1 -> A partir de un archivo (.txt) e imprimir por pantalla
Opción 2 -> A partir de un archivo (.txt) y pasarlo a otro archivo (.txt)
Opción 3 -> Introducir en la terminal e imprimir por pantalla
Opción 4 -> Introducir en la terminal y pasarlo a otro archivo (.txt)
Introduzca una opción (solo el número):

```
De la misma forma que en el menú principal, dependiendo de la opción que 
introduzca el usuario se introduce el texto que se desea justificar y se devuelve 
de la forma que el usuario desee que se devuelva
- Opción 5: Finaliza el programa

Al acabar una funcionalidad, vuelve a aparecer el menú por si el usuario desea probar
otra opción o se ha equivocado con la opción elegida
## Main

La implementación de la interfaz de usuario es relativamente sencilla. El mayor peso del programa cae sobre la función «intérprete», en la cual se llaman a todas las funciones de otros módulos y se realizan ciertas comprobaciones, como que lo introducido en ciertas funcionalidades sea realmente una palabra, y se trata la introducción de palabras en los diccionarios y el guardado de estos antes de finalizar el programa.

Además, el programa principal se ejecuta en un bucle para que la interacción con el 
usuario sea más sencilla. Por tanto, se evita reiniciar el programa cada vez que se 
quiera emplear una opción.
Para conseguir un programa más robusto, se han incluido los siguientes tratamientos 
de errores:
- Que la opción sea un número natural
- Que dicho número esté entre las opciones mostradas
- Que el usuario introduzca palabras válidas o el parámetro correcto

## Diccionario
Para hacer el tratamiento de los diccionarios se han empleado dos funciones de 
inserción, una para el diccionario general y otra para los diccionarios de rimas. 

Tienen 
este aspecto:

```python
def insertar_diccionario_general(diccionario, palabra, silabas, entonacion, rimas_cons, 
rimas_as):
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

```
De la misma forma se han empleado tres funciones de pasar de un archivo CSV a un diccionario y otras tres para hacer lo opuesto. Es cierto que se podría haber reducido 
la cantidad de funciones que tratan los archivos CSV pero, al no haber encontrado una 
alternativa que funcione, tomamos la decisión de dejarlo como está.

Las funciones tienen este aspecto:
```python
def archivo_a_diccionario_rimas_cons():
    if os.path.isfile('rimasconsonantes.csv'):
        dic = {}
        with open('rimasconsonantes.csv', 'r', newline='') as archivo:
            leer = csv.reader(archivo, delimiter=';')
            claves = next(leer) # Lee los encabezados
            for fila in leer:
                for posicion, valor in enumerate(fila):
                  clave = claves[posicion]
                  if clave not in dic:
                      dic[clave] = []
                  dic[clave].append(valor)
    else:
      dic = {}
    return dic

def diccionario_a_archivo_rima_cons(diccionario):
    print('Guardando archivo como "rimasconsonantes.csv"...')
    claves = diccionario.keys()
    filas = zip_longest(*diccionario.values(), fillvalue='')
    # El * sirve para desempaquetar los valores del diccionario
    with open('rimasconsonantes.csv', 'w', newline='') as archivo:
        escribir = csv.writer(archivo, delimiter=';')
        escribir.writerow(claves) # Pone las claves como título
        escribir.writerows(filas)
    return
```

## Silabear
#### EXPRESIONES REGULARES DE LAS NORMAS DE DIVISIÓN SILÁBICA:
### Regla 1
Una consonante entre dos vocales: V1 C V2
```regex
(?P<R1>(?i)(?P<P1>(?P<Sil1>(:?[aeiouáéíóúü]))(?P<Sil2>(:?ch|ll|rr|[bcdfgjklmnñpqrstvwxyz])(:?[aeiouáéíóúü]))))

```

### Regla 2
Dos consonantes contiguas rodeadas de vocales: V1 C1 C2 V2
```regex
(?P<R2a>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü])(?P<Sil2>[pgbcf][rl][aeiouáéíóúü])))

(?P<R2b>(?i)(?P<P1>(?P<Sil1>(:?[aeiouáéíóúü][dt]))(?P<Sil2>[r][aeiouáéíóúü])))

(?P<R2c>(?i)(?P<P1>(?P<Sil11>[aeiouáéíóúü][pgbcf])(?P<Sil21>(:?[bcdfghjkmnñpqstvwxyz]|ch|ll|rr)[aeiouáéíóúü]))|(?P<P2>(?P<Sil12>[aeiouáéíóúü][dt])(?P<Sil22>(:?[bcdfghjklmnñpqstvwxyz]|ch|ll|rr)[aeiouáéíóúü]))|(?P<P3>(?P<Sil13>[aeiouáéíóúü](:?[hjklmnñqrsvxyz]|ch|ll|rr))(?P<Sil23>(:?[bcdfghjklmnñpqrstvwxyz]|ch|ll|rr)[aeiouáéíóúü]))

```
### Regla 3
Tres consonantes contiguas entre vocales: V1 C1 C2 C3 V2
```regex
(?P<R3a>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü][bcdfghjklmnñpqrstvwxyz])(?P<Sil2>([pgbcf]|[rl][aeiouáéíóúü])|([dt][r][aeiouáéíóúü]))))

(?P<R3b>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü][bdnmlr][s])(?P<Sil2>(:?ch|ll|rr|[bcdfghjklmnñpqrstvwxyz])[aeiouáéíóúü])))

(?P<R3c>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü][s][t])(?P<Sil2>(:?ch|ll|rr|[bcdfghjklmnñpqrstvwxyz])[aeiouáéíóúü])))

```
### Regla 4
Cuatro consonantes contiguas entre vocales: V1 C1 C2 C3 C4 V2
```regex
(?P<R4>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü](:?(:?[bdnmlr][s])|(:?[s][t])))(?P<Sil2>[pgbcf][rl][aeiouáéíóúü])))

```
### Regla 5
Dos vocales consecutivas o separadas por una h: V1 V2 o V1 h V2

a) Cuando forman diptongo las vocales no se separan. 

b) Cuando forman hiato las dos vocales sí se separan por lo que la segunda sílaba comienza
en V2
```regex
(?P<R5ai>(?i)(?P<P1>(?P<Sil1>[aeoáéó](:?h?[iu]))))

(?P<R5aii>(?i)(?P<P1>(?P<Sil1>[iu](:?h?[aeoáéó]))))

(?P<R5aiii>(?i)(?P<P1>(?P<Sil1>[iuü](:?h?[iuü]))))

(?P<R5bi>(?i)(?P<P1>(?P<Sil11>[aeo])(?P<Sil21>h?[íú]))|(?P<P2>(?P<Sil12>[íú])(?P<Sil22>h?[aeo])))

(?P<R5bii>(?i)(?P<P1>(?P<Sil11>[aá])(?P<Sil21>h?[aá]))|(?P<P2>(?P<Sil12>[eé])(?P<Sil22>h?[eé]))|(?P<P3>(?P<Sil13>[ií])(?P<Sil23>h?[ií]))|(?P<P4>(?P<Sil14>[oó])(?P<Sil24>h?[oó]))|(?P<P5>(?P<Sil15>[uú])(?P<Sil25>h?[uú])))

(?P<R5biii>(?i)(?P<P1>(?P<Sil11>[aá])(?P<Sil21>h?[eéoó]))|(?P<P2>(?P<Sil12>[eé])(?P<Sil22>h?[oóaá]))|(?P<P3>(?P<Sil13>[oó])(?P<Sil23>h?[aáeé])))

```
### Regla 6
Tres vocales consecutivas: V1 V2 V3
```regex
(?P<R6>(?i)[iuü][aeoáéó][iuü])

```

### Implementación.
Para la implementación de este ejercicio ha sido esencial la función «cortar», la cual 
devuelve una lista con los cortes a realizar sobre una palabra. Esta realiza una 
búsqueda de coincidencias con las distintas expresiones regulares, calcula la posición 
del corte, se posiciona en la última vocal de la coincidencia y realiza estos pasos hasta 
que no existan más coincidencias. Todo ello se realiza guardando los cortes en una 
lista que inicialmente estará vacía.
La función «cortar» tiene esta forma:

```python
def cortar(cadena):
    cortes = [0]
    pos = 0
    res = patron2Nucleos.search(cadena, pos)
    while res:
        if res.group('R1'):
            corte = res.start() + 1
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R2a'):
                …
```

Posteriormente se emplea la función «obtener_sílabas», la cual obtiene la lista de 
cortes empleándolos como índices para separar la palabra y guardarla en una lista, 
cuyos elementos serán unidos por guiones al haber finalizado los cortes, quedando el 
resultado como un «string».
La función «obtener_silabas» tiene esta forma:
```python
def obtener_silabas(palabra):
    cortes = cortar(palabra)
    silabas = []
    for i in range(len(cortes) - 1):
        silabas.append(palabra[cortes[i]:cortes[i + 1]])
    silabas.append(palabra[cortes[-1]:])
    palabra = '-'.join(silabas)
    return palabra

```
## Entonación
Para la realización de este ejercicio, se han implementado diversas expresiones 
regulares con el fin de identificar monosílabos, agudas, llanas y esdrújulas tanto con 
tilde como sin ella.

Además, en cada expresión regular se incluyen subgrupos para la sílaba y la vocal 
tónicas. Esto también facilita la implementación de la funcionalidad de conseguir rimas 
más adelante. Para cada tipo de palabra, construimos una expresión regular teniendo 
en cuenta las reglas de acentuación, la formación de diptongos, triptongos, si ya 
llevaba tilde, y que las palabras ya van separadas por sílabas con guiones entre sí. Lo 
último nos facilita encontrar la silaba tónica según el tipo de palabra.

Para determinar la vocal tónica dentro de una sílaba tónica con varias vocales 
actuaremos así:
- En los diptongos la vocal tónica es la abierta o la segunda cerrada. 
```regex
(\w*([iuü](?P<vocal2>[iuüaeo])\w*$)
(\w*((?P<vocal3>[aeo])[iuü]\w*$)

```
- En los triptongos la vocal tónica es la central.
```regex
(\w*[iuü](?P<vocal1>[aeo])[iuüy]\w*$)

```
☝️ La terminación es adaptada a cada caso

### Monosílabos con tilde
En los monosílabos, la silaba tónica es toda la palabra y esta es siempre aguda. Ya 
tienen la tilde y no presentan guiones.
```regex
(?P<monoT>(?i)^[aeioubcdfghjklmnñpqrstvwxyz]*(?P<vocal>[áéíóú])[aeioubcdfghjklmnñpqrstvwxyz]*$)

```
### Monosílabos sin tilde
Para facilitar la realización de la expresión, ponemos solo que no lleva guiones (si 
tiene tilde, será aceptada por la expresión anterior) y añadimos el tratamiento de los 
diptongos y triptongos.

```regex
(?P<monoST>(?i)(^[^\-]\w*[iuü](?P<vocal1>[aeo])[iuüy][bcdfghjkmñpqtvwxyz]?$)|(^[^\-]\w*([iuü](?P<vocal2>[iuüaeo])\w*$)|(^[^\-]\w*((?P<vocal3>[aeo])[iuü]\w*$)|(^[^\-]\w*(?P<vocal4>[aeiou])\w*$))))

```
### Agudas con tilde
Las palabras agudas llevan tilde cuando acaban en vocal, n o s, mientras que la sílaba 
tónica es la última sílaba (lo indicamos poniendo un guion al principio y marcamos fin 
de palabra con “$”)

```regex
(?P<agudaT>(?i)[-](?P<silabaT>((\w*(?P<vocal1>[áéíóú])[ns]$)|(\w*(?P<vocal2>[áéíóú])\w+$))))
```

### Agudas sin tilde
Cuando no acaban en vocal, «n» o «s». Añadimos también la excepción de por 
ejemplo la palabra «robots» o «zigzags»: es aguda sin tilde cuando termina en «-s»
precedida de otra consonante.

```regex
(?P<agudaST>(?i)[-](?P<silabaT>(\w*[iuü](?P<vocal1>[aeo])[iuüy][bcdfghjkmñpqtvwxyz]?$)|(\w*([iuü](?P<vocal2>[iuüaeo])[bcdfghjkmñpqtvwxyz]$))|(\w*((?P<vocal3>[aeo])[iuü][bcdfghjkmñpqtvwxyz]?$)|(\w*(?P<vocal4>[aeiou])([bcdfghjkmñpqtvwxyz][ns]$|[bcdfghjklmñpqrtvwxyz]$)))))

```
### Llanas con tilde
Llevan tilde cuando no terminan en «-n», en «-s» o en vocal. Teniendo la tilde y 
sabiendo que siempre se va a encontrar en la penúltima sílaba, escribimos 
sencillamente la expresión
```regex
(?P<llanaT>(?i)(?P<silabaT>\w*(((?P<vocal>[áéíóú])))\w*)[-]\w*(?![ns])$)

```
### Llanas sin tilde
Esta fue la más complicada. Para que no se solapara con la otra regla de las agudas, 
pusimos que no llevara tildes e incluimos al final la excepción explicada en las agudas 
sin tilde, con la expresión «Negative Lookbehind (?<!)».

```regex
(?P<llanaST>(?i)(?P<silabaT>((\w*[iuü](?P<vocal1>[aeo])[iuüy])|(\w*([iuü](?P<vocal2>[aeiouü])))|(\w*(?P<vocal3>[aeo])[iuü])|(\w*(?P<vocal4>[aeiou])))\w*)[-]\w*((?<![áéíóú])[aeiouns](?<![bcdfghjklmnñpqrtvwxyz]s)$))

```
### Esdrújulas
Fue sencilla de implementar. Lleva siempre tilde en la antepenúltima sílaba 
(marcada con los guiones). La implementamos antes de las llanas para no tener 
problemas.

```regex
(?P<esdrujula>(?i)(?P<silabaT>(\w*(?P<vocal>[áéíóú])\w*))[-]\w*[-]\w+)

```
### Sobreesdrújulas
Lleva siempre tilde en la cuarta, o quinta sílaba. Para que no quedara muy larga y 
repetitiva, ponemos que «([-]\w+)» puede aparecer 3 o 4 veces. Así, contando con la 
sílaba tónica, podemos llegar a identificar más de 3 sílabas. Quedando la tilde en la 
cuarta, o quinta sílaba, que es lo que necesitamos buscar.
```regex
(?P<sobreesdrujula>(?i)(?P<silabaT>(\w*(?P<vocal>[áéíóú])\w*))([-]\w+){3,4}$)

```

### Implementación.
La función principal de esta implementación es «entonacion». Esta recibe la palabra 
separada por sílabas y realiza sobre ella la búsqueda de las expresiones regulares 
definidas. Devuelve las sílabas con la acentuación en mayúscula, el tipo, la sílaba 
tónica y la vocal tónica.
Un pequeño extracto de esta función es:

```python
elif res.group('agudaST'):
    tipo_palabra = 'aguda'
    silaba_t = res.group('silabaT')
    if res.group('vocal1'):
        vocal_acentuada = res.group('vocal1')
    elif res.group('vocal2'):
        vocal_acentuada = res.group('vocal2')
    elif res.group('vocal3'):
        vocal_acentuada = res.group('vocal3')
    elif res.group('vocal4'):
        vocal_acentuada = res.group('vocal4'
```

Como hay diversas opciones para la vocal tónica, agregamos diversos condicionales.
Adicionalmente, para reemplazar en la palabra la vocal tónica, y ponerla en mayúscula
sin tildes, implementamos dos funciones auxiliares: una para reemplazar la vocal 
tónica y otra para reemplazar en la palabra. Así dividimos en subproblemas, y se hace 
más sencilla la implementación.

## Rimas
Contamos con dos funciones para calcular las terminaciones de las rimas. Con la 
función de entonación, obtenemos la silaba y la vocal tónica. En ambos casos, se 
devuelve la vocal tónica ya en mayúscula. Para identificar la rima, necesitamos el resto 
de la palabra a partir de la vocal tónica.
- terminación_asonante(palabra): incluye solo las vocales desde la vocal tónica
- terminación_ consonante(palabra): incluye todas las letras de la vocal tónica
En ambos casos la implementación es casi idéntica. Solo cambia la manera de coger 
la terminación, y para ello necesitamos saber el índice de la vocal tónica en la palabra.
### 1) Obtenemos las sílabas
```python
silabas = silabar.obtener_silabas(palabra.strip())

```
### 2) Con la función «entonacion» obtenemos las silabas con la entonación 
marcada, la silaba tónica también con la entonación marcada y la vocal tónica, 
también en mayúscula. Así, en casos como la palabra «melocotón», no nos 
molesta la tilde para asociarla como rima consonante a la palabra «son». En 
este caso, el tipo no nos interesa, por lo que lo marcamos con «_», para no 
usar variables innecesarias.
```python
silabas_entonadas, _, silaba_t, vocal_t = entonar.entonacion(silabas)

```
### 3) Quitamos los guiones de la palabra entonada
```python
palabra2 = silabas_entonadas.replace("-", "")

```

### 4) Para encontrar el índice de donde empieza la sílaba tónica podemos usar «find». Al igual con donde empieza la vocal tónica dentro de la sílaba tónica
```python
indice_silaba_tonica = palabra2.find(silaba_t)
indice_vocal_tonica_silaba = silaba_t.find(vocal_t)

```
### 5) La suma de ambos resulta en el índice de la vocal tónica en la palabra
```python
indice_vocal_tonica = indice_silaba_tonica + indice_vocal_tonica_silaba

```

## Justificar
El comienzo de este ejercicio comienza en la función «interprete_justificar». Este actúa 
según lo indicado por el usuario (si quiere obtener el texto a justificar de un fichero o 
desde la terminal y si desea imprimirlo por pantalla o guardarlo en otro fichero). Para 
los ficheros, se ha hecho que sea necesario que sean ficheros de texto, cuya 
extensión sea «.txt».
En esta función se han hecho tratamientos de errores relativos al ancho, pues debe 
ser un número natural. Además, si la opción elegida por el usuario no se encuentra 
entre las opciones ofertadas, el programa no parará e imprimirá la razón por la que no 
se está justificando el texto.

El intérprete llama a la función «justificar_texto» la cual carga con el peso de esta 
implementación. Esta lee las líneas del texto y, si no están vacías, separa las palabras 
en listas de sílabas y las junta agregando los espacios. Trata la primera y la última 
línea de la sílaba por separado, añadiendo a un «string» las sílabas conforme sea 
conveniente y añadiendo estos a una lista de líneas que luego serán juntadas con 
retornos de carro.
El tratamiento de las sílabas varía según si la suma de la longitud de la línea actual, 
distinta de la línea del texto introducido por el usuario, con la sílaba (más algún 
elemento especial que vaya a añadir) es menor, igual o mayor al ancho deseado. 
Según si estas sílabas son monosílabas, el inicio o fin de una palabra o una sílaba 
entre otras sílabas añade un guion y las deja para la siguiente línea, únicamente las 
deja para la siguiente línea o las añade a la línea actual.
Un pequeño extracto representativo de esta función es:

```python
elif lista_silabas[contador - 1] == ' ': # principio de una palabra
    texto_justificado.append(justificar_linea(linea_actual[:-1], ancho))
    linea_actual = silaba
else:
    linea_actual = linea_actual + '-'
    texto_justificado.append(justificar_linea(linea_actual, ancho))
    linea_actual = silaba

```
Finalmente, para las líneas que se quedan cortas de ancho al haber terminado con su 
tratamiento, se emplea la función «justificar línea», la cual devuelve una línea a la cual 
se le han aplicado más espacios para que corresponda con el ancho deseado.

Es apreciable que el resultado de este ejercicio no siempre es preciso y, en ocasiones, 
el ancho resultante es mínimamente mayor que el deseado. Esto es debido a una 
mala gestión de tiempo por parte del equipo, el cual ha hecho que no se pueda 
trabajar más en mejorar esta parte del programa.


