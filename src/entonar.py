import regex as re

ER = (
    r'(?P<monoT>(?i)^[aeioubcdfghjklmnñpqrstvwxyz]*(?P<vocal>[áéíóú])[aeioubcdfghjklmnñpqrstvwxyz]*$)|(?P<monoST>(?i)(^[^\-]\w*[iuü](?P<vocal1>[aeo])[iuüy][bcdfghjkmñpqtvwxyz]?$)|(^[^\-]\w*([iuü](?P<vocal2>[iuüaeo])\w*$)|(^[^\-]\w*((?P<vocal3>[aeo])[iuü]\w*$)|(^[^\-]\w*(?P<vocal4>[aeiou])\w*$))))|(?P<agudaT>(?i)[-](?P<silabaT>((\w*(?P<vocal1>[áéíóú])[ns]$)|(\w*(?P<vocal2>[áéíóú])\w+$))))|(?P<agudaST>(?i)[-](?P<silabaT>(\w*[iuü](?P<vocal1>[aeo])[iuüy][bcdfghjkmñpqtvwxyz]?$)|(\w*([iuü](?P<vocal2>[iuüaeo])[bcdfghjkmñpqtvwxyz]$))|(\w*((?P<vocal3>[aeo])[iuü][bcdfghjkmñpqtvwxyz]?$)|(\w*(?P<vocal4>[aeiou])([bcdfghjkmñpqtvwxyz][ns]$|[bcdfghjklmñpqrtvwxyz]$)))))|(?P<sobreesdrujula>(?i)(?P<silabaT>(\w*(?P<vocal>[áéíóú])\w*))([-]\w+){3,4}$)|(?P<esdrujula>(?i)(?P<silabaT>(\w*(?P<vocal>[áéíóú])\w*))[-]\w*[-]\w+)|(?P<llanaT>(?i)(?P<silabaT>\w*(((?P<vocal>[áéíóú])))\w*)[-]\w*(?![ns])$)|(?P<llanaST>(?i)(?P<silabaT>((\w*[iuü](?P<vocal1>[aeo])[iuüy])|(\w*([iuü](?P<vocal2>[aeiouü])))|(\w*(?P<vocal3>[aeo])[iuü])|(\w*(?P<vocal4>[aeiou])))\w*)[-]\w*((?<![áéíóú])[aeiouns](?<![bcdfghjklmnñpqrtvwxyz]s)$))')

patron = re.compile(ER)


# Función auxiliar para cambiar las vocales acentuadas
def reemplazar_vocal(caracter):
    if caracter in 'Á,á,a':
        caracter = 'A'
    elif caracter in 'É,é,e':
        caracter = 'E'
    elif caracter in 'Í,í,i':
        caracter = 'I'
    elif caracter in 'Ó,ó,o':
        caracter = 'O'
    elif caracter in 'Ú,ú,u':
        caracter = 'U'

    return caracter


def reemplazar_palabra(silabas, silaba_tonica, vocal_acentuada):
    indice_silaba_tonica = silabas.find(silaba_tonica)

    # Reemplaza solo la vocal acentuada en la sílaba tónica
    parte_antes = silabas[:indice_silaba_tonica]
    parte_despues = silabas[indice_silaba_tonica:].replace(vocal_acentuada, reemplazar_vocal(vocal_acentuada), 1)

    silabas = parte_antes + parte_despues

    return silabas


def entonacion(silabas):
    pos = 0
    tipo_palabra = ''
    lista_silabas = ''
    silaba_t = ''
    vocal_acentuada = ''
    res = patron.search(silabas, pos)
    while res:

        if res.group('monoT'):
            tipo_palabra = 'aguda'
            vocal_acentuada = res.group('vocal')

            pos = res.end() - 1

            lista_silabas = reemplazar_palabra(silabas, silaba_t, vocal_acentuada)
            silaba_t = lista_silabas
            vocal_acentuada = reemplazar_vocal(vocal_acentuada)

        elif res.group('monoST'):
            tipo_palabra = 'aguda'
            if res.group('vocal1'):
                vocal_acentuada = res.group('vocal1')
            elif res.group('vocal2'):
                vocal_acentuada = res.group('vocal2')
            elif res.group('vocal3'):
                vocal_acentuada = res.group('vocal3')
            elif res.group('vocal4'):
                vocal_acentuada = res.group('vocal4')

            pos = res.end() - 1

            lista_silabas = reemplazar_palabra(silabas, silaba_t, vocal_acentuada)
            silaba_t = lista_silabas
            vocal_acentuada = reemplazar_vocal(vocal_acentuada)

        elif res.group('agudaT'):
            tipo_palabra = 'aguda'
            silaba_t = res.group('silabaT')
            if res.group('vocal1'):
                vocal_acentuada = res.group('vocal1')
            elif res.group('vocal2'):
                vocal_acentuada = res.group('vocal2')

            pos = res.end() - 1

            lista_silabas = reemplazar_palabra(silabas, silaba_t, vocal_acentuada)
            silaba_t = silaba_t.replace(vocal_acentuada, reemplazar_vocal(vocal_acentuada))
            vocal_acentuada = reemplazar_vocal(vocal_acentuada)

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
                vocal_acentuada = res.group('vocal4')

            pos = res.end() - 1

            lista_silabas = reemplazar_palabra(silabas, silaba_t, vocal_acentuada)
            silaba_t = silaba_t.replace(vocal_acentuada, reemplazar_vocal(vocal_acentuada))
            vocal_acentuada = reemplazar_vocal(vocal_acentuada)

        elif res.group('sobreesdrujula'):
            tipo_palabra = 'sobreesdrújula'
            silaba_t = res.group('silabaT')
            vocal_acentuada = res.group('vocal')

            pos = res.end() - 1

            lista_silabas = reemplazar_palabra(silabas, silaba_t, vocal_acentuada)
            silaba_t = silaba_t.replace(vocal_acentuada, reemplazar_vocal(vocal_acentuada))
            vocal_acentuada = reemplazar_vocal(vocal_acentuada)

        elif res.group('esdrujula'):
            tipo_palabra = 'esdrújula'
            silaba_t = res.group('silabaT')
            vocal_acentuada = res.group('vocal')

            pos = res.end() - 1

            lista_silabas = reemplazar_palabra(silabas, silaba_t, vocal_acentuada)
            silaba_t = silaba_t.replace(vocal_acentuada, reemplazar_vocal(vocal_acentuada))
            vocal_acentuada = reemplazar_vocal(vocal_acentuada)

        elif res.group('llanaT'):
            tipo_palabra = 'llana'
            silaba_t = res.group('silabaT')
            vocal_acentuada = res.group('vocal')

            pos = res.end() - 1

            lista_silabas = reemplazar_palabra(silabas, silaba_t, vocal_acentuada)
            silaba_t = silaba_t.replace(vocal_acentuada, reemplazar_vocal(vocal_acentuada))
            vocal_acentuada = reemplazar_vocal(vocal_acentuada)

        elif res.group('llanaST'):
            tipo_palabra = 'llana'
            silaba_t = res.group('silabaT')
            if res.group('vocal1'):
                vocal_acentuada = res.group('vocal1')
            elif res.group('vocal2'):
                vocal_acentuada = res.group('vocal2')
            elif res.group('vocal3'):
                vocal_acentuada = res.group('vocal3')
            elif res.group('vocal4'):
                vocal_acentuada = res.group('vocal4')

            pos = res.end() - 1

            lista_silabas = reemplazar_palabra(silabas, silaba_t, vocal_acentuada)
            silaba_t = silaba_t.replace(vocal_acentuada, reemplazar_vocal(vocal_acentuada))
            vocal_acentuada = reemplazar_vocal(vocal_acentuada)

        res = patron.search(silabas, pos)

    return lista_silabas, tipo_palabra, silaba_t, vocal_acentuada
