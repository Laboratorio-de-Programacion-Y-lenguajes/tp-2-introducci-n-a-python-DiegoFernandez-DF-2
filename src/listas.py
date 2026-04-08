# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    # TU CÓDIGO AQUÍ
    total = 0

    for numero in numeros:
        total += numero

    return total


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    # TU CÓDIGO AQUÍ
    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    # TU CÓDIGO AQUÍ
    lista_invertida = []

    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])

    return lista_invertida


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    # TU CÓDIGO AQUÍ
    resultado = []

    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)

    return resultado


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    # TU CÓDIGO AQUÍ
    resultado = []

    for sublista in lista:
        for elemento in sublista:
            resultado.append(elemento)

    return resultado
