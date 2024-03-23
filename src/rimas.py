import silabar
import entonar


def terminacion_asonante(palabra):
    silabas = silabar.obtener_silabas(palabra.strip())
    silabas_entonadas, _, silaba_t, vocal_t = entonar.entonacion(silabas)

    palabra2 = silabas_entonadas.replace("-", "")

    indice_silaba_tonica = palabra2.find(silaba_t)
    indice_vocal_tonica_silaba = silaba_t.find(vocal_t)
    indice_vocal_tonica = indice_silaba_tonica + indice_vocal_tonica_silaba

    # Todas las vocales desde la sílaba tónica hasta el final
    terminacion = '-'.join([c for c in palabra2[indice_vocal_tonica:] if c in 'AEIOUaeiouáéíóúüy'])
    return terminacion


def terminacion_consonante(palabra):
    silabas = silabar.obtener_silabas(palabra.strip())
    silabas_entonadas, _, silaba_t, vocal_t = entonar.entonacion(silabas)

    palabra2 = silabas_entonadas.replace("-", "")

    indice_silaba_tonica = palabra2.find(silaba_t)
    indice_vocal_tonica_silaba = silaba_t.find(vocal_t)
    indice_vocal_tonica = indice_silaba_tonica + indice_vocal_tonica_silaba
    terminacion = palabra2[indice_vocal_tonica:]
    return terminacion
