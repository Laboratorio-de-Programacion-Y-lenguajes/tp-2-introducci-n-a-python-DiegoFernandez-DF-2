# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    # TU CÓDIGO AQUÍ
    texto_normalizado = ""

    for caracter in texto.lower():
        if caracter.isalnum():
            texto_normalizado += caracter

    return texto_normalizado == texto_normalizado[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    # TU CÓDIGO AQUÍ
    palabras = texto.split()
    resultado = []

    for palabra in palabras:
        if palabra:
            palabra_capitalizada = palabra[0].upper() + palabra[1:].lower()
            resultado.append(palabra_capitalizada)

    return " ".join(resultado)


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    # TU CÓDIGO AQUÍ
    vocales = "aeiou"
    contador = 0

    for caracter in texto.lower():
        if caracter in vocales:
            contador += 1

    return contador


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    # TU CÓDIGO AQUÍ
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            if caracter.islower():
                base = ord('a')
            else:
                base = ord('A')

            posicion = ord(caracter) - base
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado += chr(base + nueva_posicion)
        else:
            resultado += caracter

    return resultado
