# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    """
    Retorna un diccionario con la frecuencia de cada palabra.
    Ejemplo: contar_palabras("hola mundo hola") -> {"hola": 2, "mundo": 1}
    Las palabras deben ser comparadas en minúsculas.
    """
    # TU CÓDIGO AQUÍ
    conteo = {}
    palabras = texto.lower().split()

    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    return conteo


def invertir_diccionario(d: dict) -> dict:
    """
    Retorna un nuevo diccionario con claves y valores intercambiados.
    Ejemplo: invertir_diccionario({"a": 1}) -> {1: "a"}
    """
    # TU CÓDIGO AQUÍ
    invertido = {}

    for clave, valor in d.items():
        invertido[valor] = clave

    return invertido


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """
    Combina dos diccionarios. Si hay claves repetidas, prevalece d2.
    """
    # TU CÓDIGO AQUÍ
    resultado = {}

    for clave, valor in d1.items():
        resultado[clave] = valor

    for clave, valor in d2.items():
        resultado[clave] = valor

    return resultado


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """
    Retorna un nuevo diccionario con solo los pares
    cuyo valor sea >= minimo.
    """
    # TU CÓDIGO AQUÍ
    resultado = {}

    for clave, valor in d.items():
        if valor >= minimo:
            resultado[clave] = valor

    return resultado
