import regex as re

ER2Nucleos = r'(?P<R1>(?i)(?P<P1>(?P<Sil1>(:?[aeiouáéíóúü]))(?P<Sil2>(:?ch|ll|rr|[bcdfgjklmnñpqrstvwxyz])(:?[aeiouáéíóúü]))))|(?P<R2a>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü])(?P<Sil2>[pgbcf][rl][aeiouáéíóúü])))|(?P<R2b>(?i)(?P<P1>(?P<Sil1>(:?[aeiouáéíóúü][dt]))(?P<Sil2>[r][aeiouáéíóúü])))|(?P<R2c>(?i)(?P<P1>(?P<Sil11>[aeiouáéíóúü][pgbcf])(?P<Sil21>(:?[bcdfghjkmnñpqstvwxyz]|ch|ll|rr)[aeiouáéíóúü]))|(?P<P2>(?P<Sil12>[aeiouáéíóúü][dt])(?P<Sil22>(:?[bcdfghjklmnñpqstvwxyz]|ch|ll|rr)[aeiouáéíóúü]))|(?P<P3>(?P<Sil13>[aeiouáéíóúü](:?[hjklmnñqrsvxyz]|ch|ll|rr))(?P<Sil23>(:?[bcdfghjklmnñpqrstvwxyz]|ch|ll|rr)[aeiouáéíóúü])))|(?P<R3a>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü][bcdfghjklmnñpqrstvwxyz])(?P<Sil2>([pgbcf]|[rl][aeiouáéíóúü])|([dt][r][aeiouáéíóúü]))))|(?P<R3b>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü][bdnmlr][s])(?P<Sil2>(:?ch|ll|rr|[bcdfghjklmnñpqrstvwxyz])[aeiouáéíóúü])))|(?P<R3c>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü][s][t])(?P<Sil2>(:?ch|ll|rr|[bcdfghjklmnñpqrstvwxyz])[aeiouáéíóúü])))|(?P<R4>(?i)(?P<P1>(?P<Sil1>[aeiouáéíóúü](:?(:?[bdnmlr][s])|(:?[s][t])))(?P<Sil2>[pgbcf][rl][aeiouáéíóúü])))|(?P<R6>(?i)[iuü][aeoáéó][iuü])|(?P<R5ai>(?i)(?P<P1>(?P<Sil1>[aeoáéó](:?h?[iu]))))|(?P<R5aii>(?i)(?P<P1>(?P<Sil1>[iu](:?h?[aeoáéó]))))|(?P<R5aiii>(?i)(?P<P1>(?P<Sil1>[iuü](:?h?[iuü]))))|(?P<R5bi>(?i)(?P<P1>(?P<Sil11>[aeo])(?P<Sil21>h?[íú]))|(?P<P2>(?P<Sil12>[íú])(?P<Sil22>h?[aeo])))|(?P<R5bii>(?i)(?P<P1>(?P<Sil11>[aá])(?P<Sil21>h?[aá]))|(?P<P2>(?P<Sil12>[eé])(?P<Sil22>h?[eé]))|(?P<P3>(?P<Sil13>[ií])(?P<Sil23>h?[ií]))|(?P<P4>(?P<Sil14>[oó])(?P<Sil24>h?[oó]))|(?P<P5>(?P<Sil15>[uú])(?P<Sil25>h?[uú])))|(?P<R5biii>(?i)(?P<P1>(?P<Sil11>[aá])(?P<Sil21>h?[eéoó]))|(?P<P2>(?P<Sil12>[eé])(?P<Sil22>h?[oóaá]))|(?P<P3>(?P<Sil13>[oó])(?P<Sil23>h?[aáeé])))'
# La regla 1 no tiene h en las consonantes porque es parte de otra regla
patron2Nucleos = re.compile(ER2Nucleos)


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
            corte = res.start() + 1
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R2b'):
            corte = res.start() + 1
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R2c'):
            corte = res.start() + 2
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R3a'):
            corte = res.start() + 2
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R3b'):
            corte = res.start() + 3
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R3c'):
            corte = res.start() + 3
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R4'):
            corte = res.start() + 3
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R6'):
            pos = res.end() - 1
        elif res.group('R5ai'):
            pos = res.end() - 1
        elif res.group('R5aii'):
            pos = res.end() - 1
        elif res.group('R5aiii'):
            pos = res.end() - 1
        elif res.group('R5bi'):
            corte = res.start() + 1
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R5bii'):
            corte = res.start() + 1
            cortes.append(corte)
            pos = res.end() - 1
        elif res.group('R5biii'):
            corte = res.start() + 1
            cortes.append(corte)
            pos = res.end() - 1

        res = patron2Nucleos.search(cadena, pos)
    return cortes


def obtener_silabas(palabra):
    cortes = cortar(palabra)
    silabas = []

    for i in range(len(cortes) - 1):
        silabas.append(palabra[cortes[i]:cortes[i + 1]])
    silabas.append(palabra[cortes[-1]:])

    palabra = '-'.join(silabas)

    return palabra
