# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: ChatGPT

**Prompt usado**:
**Role:** Eres un tutor de Python 3.13 especialista en algoritmos matemáticos.

**Restricciones:**- Sin imports. Solo built-ins de Python- Seguir PEP 8 estrictamente- Compatible con Python 3.13, Código claro: nombres descriptivos, sin duplicación innecesaria. Yo ejecutare el codigo y los tests localmente en PyCharm

Necesito una implementación de codigo que pueda aprobar todos los siguientes tests en python:

def test_crear_saludo_simple():
    assert crear_saludo("Ana") == "Hola, Ana!"


def test_crear_saludo_otro_nombre():
    assert crear_saludo("Juan") == "Hola, Juan!"


def test_suma_enteros_positivos():
    assert suma_enteros(3, 4) == 7


def test_suma_enteros_negativos():
    assert suma_enteros(-2, -3) == -5


def test_suma_enteros_mixtos():
    assert suma_enteros(-1, 1) == 0


def test_es_mayor_de_edad_true():
    assert es_mayor_de_edad(18) is True
    assert es_mayor_de_edad(25) is True


def test_es_mayor_de_edad_false():
    assert es_mayor_de_edad(17) is False
    assert es_mayor_de_edad(0) is False


def test_tipo_de_dato_int():
    assert tipo_de_dato(42) == "int"


def test_tipo_de_dato_str():
    assert tipo_de_dato("hola") == "str"


def test_tipo_de_dato_float():
    assert tipo_de_dato(3.14) == "float"


def test_tipo_de_dato_bool():
    assert tipo_de_dato(True) == "bool"


def test_convertir_a_float():
    assert convertir_a_float("3.14") == 3.14
    assert convertir_a_float("0") == 0.0


**Resultado obtenido**:
def crear_saludo(nombre: str) -> str:
    return f"Hola, {nombre}!"


def suma_enteros(a: int, b: int) -> int:
    return a + b


def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18


def tipo_de_dato(valor) -> str:
    if isinstance(valor, bool):
        return "bool"
    if isinstance(valor, int):
        return "int"
    if isinstance(valor, float):
        return "float"
    if isinstance(valor, str):
        return "str"
    return type(valor).__name__


def convertir_a_float(valor: str) -> float:
    return float(valor)


**¿Lo usaste tal cual o lo modificaste?**
No entiendo a que se refiere con esta pregunta pero use lo que me interesaba del prompt recomendado de la guia de propmts de la materia y agregué o cambié lo que yo consideré necesario.

---

### 2 - condicionales.py

**Herramienta**: ChatGPT

**Prompt usado**:
**Role:** Eres un tutor de Python 3.13 especialista en algoritmos matemáticos. 

**Restricciones:**- Sin imports. Solo built-ins de Python- Seguir PEP 8 estrictamente- Compatible con Python 3.13, Código claro: nombres descriptivos, sin duplicación innecesaria. Yo ejecutare el codigo y los tests localmente en PyCharm

Necesito una implementación de codigo que pueda aprobar todos los siguientes tests en python:

def test_clasificar_numero_positivo():
    assert clasificar_numero(5) == "positivo"


def test_clasificar_numero_negativo():
    assert clasificar_numero(-3) == "negativo"


def test_clasificar_numero_cero():
    assert clasificar_numero(0) == "cero"


def test_mayor_de_tres():
    assert mayor_de_tres(1, 2, 3) == 3
    assert mayor_de_tres(5, 3, 4) == 5
    assert mayor_de_tres(2, 7, 1) == 7


def test_clasificar_nota_sobresaliente():
    assert clasificar_nota(9) == "Sobresaliente"
    assert clasificar_nota(10) == "Sobresaliente"


def test_clasificar_nota_bueno():
    assert clasificar_nota(7) == "Bueno"
    assert clasificar_nota(8) == "Bueno"


def test_clasificar_nota_aprobado():
    assert clasificar_nota(6) == "Aprobado"


def test_clasificar_nota_desaprobado():
    assert clasificar_nota(5) == "Desaprobado"
    assert clasificar_nota(0) == "Desaprobado"


def test_es_bisiesto_true():
    assert es_bisiesto(2000) is True
    assert es_bisiesto(2024) is True


def test_es_bisiesto_false():
    assert es_bisiesto(1900) is False
    assert es_bisiesto(2023) is False


**Resultado obtenido**:
def clasificar_numero(numero: int) -> str:
    if numero > 0:
        return "positivo"
    if numero < 0:
        return "negativo"
    return "cero"


def mayor_de_tres(a: int, b: int, c: int) -> int:
    mayor = a

    if b > mayor:
        mayor = b

    if c > mayor:
        mayor = c

    return mayor


def clasificar_nota(nota: int) -> str:
    if nota >= 9:
        return "Sobresaliente"
    if nota >= 7:
        return "Bueno"
    if nota == 6:
        return "Aprobado"
    return "Desaprobado"


def es_bisiesto(anio: int) -> bool:
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    return anio % 4 == 0


**¿Lo usaste tal cual o lo modificaste?**
Es identico al prompt 1 salvo por el test que envío

---

### 3 - listas.py

**Herramienta**: ChatGPT

**Prompt usado**:
**Role:** Eres un tutor de Python 3.13 especialista en algoritmos matemáticos. 

**Restricciones:**- Sin imports. Solo built-ins de Python- Seguir PEP 8 estrictamente- Compatible con Python 3.13, Código claro: nombres descriptivos, sin duplicación innecesaria. Yo ejecutare el codigo y los tests localmente en PyCharm

Necesito una implementación de codigo que pueda aprobar todos los siguientes tests en python:

def test_suma_lista():
    assert suma_lista([1, 2, 3, 4]) == 10
    assert suma_lista([]) == 0
 

def test_filtrar_pares():
    assert filtrar_pares([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filtrar_pares([1, 3, 5]) == []
 

def test_invertir_lista_no_modifica_original():
    original = [1, 2, 3]
    resultado = invertir_lista(original)
    assert resultado == [3, 2, 1]
    assert original == [1, 2, 3]
 

def test_eliminar_duplicados():
    assert eliminar_duplicados([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert eliminar_duplicados([1, 1, 1]) == [1] 
 

def test_eliminar_duplicados_orden():
    assert eliminar_duplicados([3, 1, 2, 1, 3]) == [3, 1, 2] 
 

def test_aplanar_lista():
    assert aplanar_lista([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert aplanar_lista([[1], [2], [3]]) == [1, 2, 3]


**Resultado obtenido**:
def suma_lista(numeros: list[int]) -> int:
    total = 0

    for numero in numeros:
        total += numero

    return total


def filtrar_pares(numeros: list[int]) -> list[int]:
    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares


def invertir_lista(lista: list[int]) -> list[int]:
    lista_invertida = []

    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])

    return lista_invertida


def eliminar_duplicados(lista: list[int]) -> list[int]:
    resultado = []

    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)

    return resultado


def aplanar_lista(lista_de_listas: list[list[int]]) -> list[int]:
    resultado = []

    for sublista in lista_de_listas:
        for elemento in sublista:
            resultado.append(elemento)

    return resultado


**¿Lo usaste tal cual o lo modificaste?**
Es identico al prompt 1 salvo por el test que envío. Tuve que utilizar el siguiente prompt:

necesito que los llamados de las funciones sean los siguientes y hagas cambios en el codigo en base a ellos en caso de ser necesario: 

def suma_lista(numeros: list) -> int | float: def filtrar_pares(numeros: list) -> list: def invertir_lista(lista: list) -> list: def eliminar_duplicados(lista: list) -> list: def aplanar_lista(lista: list) -> list:


La IA siguiendo mis indicaciones, cambio la siguiente función:

def aplanar_lista(lista: list) -> list:
    resultado = []

    for sublista in lista:
        for elemento in sublista:
            resultado.append(elemento)

    return resultado

---

### 4 - diccionarios.py

**Herramienta**: ChatGPT

**Prompt usado**:
**Role:** Eres un tutor de Python 3.13 especialista en algoritmos matemáticos.  

**Restricciones:**- Sin imports. Solo built-ins de Python- Seguir PEP 8 estrictamente- Compatible con Python 3.13, Código claro: nombres descriptivos, sin duplicación innecesaria. 

Yo ejecutare el codigo y los tests localmente en PyCharm Necesito una implementación de codigo que pueda aprobar todos los siguientes tests en python:

def test_contar_palabras():
    assert contar_palabras("hola mundo hola") == {"hola": 2, "mundo": 1} 
 

def test_contar_palabras_case_insensitive():
    assert contar_palabras("Hola hola") == {"hola": 2} 
 

def test_invertir_diccionario():
    assert invertir_diccionario({"a": 1, "b": 2}) == {1: "a", 2: "b"} 
 

def test_merge_diccionarios_sin_conflicto():
    assert merge_diccionarios({"a": 1}, {"b": 2}) == {"a": 1, "b": 2} 
 

def test_merge_diccionarios_con_conflicto():
    assert merge_diccionarios({"a": 1}, {"a": 99}) == {"a": 99} 
 

def test_filtrar_por_valor():
    assert filtrar_por_valor({"a": 5, "b": 10, "c": 3}, 5) == {"a": 5, "b": 10}

Necesito que los llamados de las funciones sean los siguientes:

def contar_palabras(texto: str) -> dict:

def invertir_diccionario(d: dict) -> dict:

def merge_diccionarios(d1: dict, d2: dict) -> dict:

def filtrar_por_valor(d: dict, minimo: int) -> dict:


**Resultado obtenido**:
def contar_palabras(texto: str) -> dict:
    conteo = {}
    palabras = texto.lower().split()

    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    return conteo


def invertir_diccionario(d: dict) -> dict:
    invertido = {}

    for clave, valor in d.items():
        invertido[valor] = clave

    return invertido


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    resultado = {}

    for clave, valor in d1.items():
        resultado[clave] = valor

    for clave, valor in d2.items():
        resultado[clave] = valor

    return resultado


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    resultado = {}

    for clave, valor in d.items():
        if valor >= minimo:
            resultado[clave] = valor

    return resultado

**¿Lo usaste tal cual o lo modificaste?**
Es identico al prompt 1 salvo por el test, pero de ahora en adelante indico como deben estar estructurados los llamados para evitar corregirlos como en el ejercicio 3 "listas.py"

---

### 5 - loops.py

**Herramienta**: ChatGPT

**Prompt usado**:
**Role:** Eres un tutor de Python 3.13 especialista en algoritmos matemáticos. 

**Restricciones:**- Sin imports. Solo built-ins de Python- Seguir PEP 8 estrictamente- Compatible con Python 3.13, Código claro: nombres descriptivos, sin duplicación innecesaria. 

Yo ejecutare el codigo y los tests localmente en PyCharm Necesito una implementación de codigo que pueda aprobar todos los siguientes tests en python:

def test_contar_hasta():
    assert contar_hasta(5) == [1, 2, 3, 4, 5]
    assert contar_hasta(1) == [1] 
 

def test_tabla_multiplicar():
    assert tabla_multiplicar(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30] 
 

def test_suma_digitos():
    assert suma_digitos(123) == 6
    assert suma_digitos(0) == 0 
 

def test_es_primo_true():
    assert es_primo(2) is True
    assert es_primo(7) is True
    assert es_primo(13) is True 
 

def test_es_primo_false():
    assert es_primo(1) is False
    assert es_primo(4) is False
    assert es_primo(9) is False 
 

def test_fibonacci():
    assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
    assert fibonacci(1) == [0]

Necesito que los llamados de las funciones sean los siguientes:

def contar_hasta(n: int) -> list:

def tabla_multiplicar(n: int) -> list:

def suma_digitos(n: int) -> int:

def es_primo(n: int) -> bool:

def fibonacci(n: int) -> list:


**Resultado obtenido**:
def contar_hasta(n: int) -> list:
    resultado = []

    for i in range(1, n + 1):
        resultado.append(i)

    return resultado


def tabla_multiplicar(n: int) -> list:
    resultado = []

    for i in range(1, 11):
        resultado.append(n * i)

    return resultado


def suma_digitos(n: int) -> int:
    total = 0

    for digito in str(n):
        total += int(digito)

    return total


def es_primo(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def fibonacci(n: int) -> list:
    if n <= 0:
        return []

    if n == 1:
        return [0]

    resultado = [0, 1]

    while len(resultado) < n:
        siguiente = resultado[-1] + resultado[-2]
        resultado.append(siguiente)

    return resultado


**¿Lo usaste tal cual o lo modificaste?**
Es identico al prompt 1 salvo por el test, pero de ahora en adelante indico como deben estar estructurados los llamados para evitar corregirlos como en el ejercicio 3 "listas.py"

---

### 6 - funciones.py

**Herramienta**: ChatGPT

**Prompt usado**:
**Role:** Eres un tutor de Python 3.13 especialista en algoritmos matemáticos. 

**Restricciones:**- Sin imports. Solo built-ins de Python- Seguir PEP 8 estrictamente- Compatible con Python 3.13, Código claro: nombres descriptivos, sin duplicación innecesaria. 

Yo ejecutare el codigo y los tests localmente en PyCharm Necesito una implementación de codigo que pueda aprobar todos los siguientes tests en python:

def test_aplicar_funcion():
    assert aplicar_funcion([1, 2, 3], lambda x: x * 2) == [2, 4, 6] 
 

def test_componer():
    doble = lambda x: x * 2
    sumar_uno = lambda x: x + 1
    doble_luego_sumar = componer(sumar_uno, doble)
    assert doble_luego_sumar(3) == 7  # sumar_uno(doble(3)) = 7 
 

def test_memoizar():
    llamadas = [] 
 
    def costosa(n):
        llamadas.append(n)
        return n * 2

    func_memo = memoizar(costosa)
    assert func_memo(5) == 10
    assert func_memo(5) == 10
    assert len(llamadas) == 1  # solo se ejecutó una vez 
 

def test_reducir():
    assert reducir([1, 2, 3, 4], lambda a, b: a + b, 0) == 10
    assert reducir([1, 2, 3], lambda a, b: a * b, 1) == 6


Necesito que los llamados de las funciones sean los siguientes:

def aplicar_funcion(lista: list, func) -> list:

def componer(f, g):

def memoizar(func):

def reducir(lista: list, func, inicial):


**Resultado obtenido**:
def aplicar_funcion(lista: list, func) -> list:
    resultado = []

    for elemento in lista:
        resultado.append(func(elemento))

    return resultado


def componer(f, g):
    def funcion_compuesta(x):
        return f(g(x))

    return funcion_compuesta


def memoizar(func):
    cache = {}

    def funcion_memoizada(arg):
        if arg not in cache:
            cache[arg] = func(arg)
        return cache[arg]

    return funcion_memoizada


def reducir(lista: list, func, inicial):
    acumulador = inicial

    for elemento in lista:
        acumulador = func(acumulador, elemento)

    return acumulador


**¿Lo usaste tal cual o lo modificaste?**
Es identico al prompt 1 salvo por el test, pero de ahora en adelante indico como deben estar estructurados los llamados para evitar corregirlos como en el ejercicio 3 "listas.py"

---

### 7 - operaciones.py

**Herramienta**: ChatGPT

**Prompt usado**:
**Role:** Eres un tutor de Python 3.13 especialista en algoritmos matemáticos.

**Restricciones:**- Sin imports. Solo built-ins de Python- Seguir PEP 8 estrictamente- Compatible con Python 3.13, Código claro: nombres descriptivos, sin duplicación innecesaria. 

Yo ejecutare el codigo y los tests localmente en PyCharm Necesito una implementación de codigo que pueda aprobar todos los siguientes tests en python:

def test_es_palindromo_true():
    assert es_palindromo("ana") is True
    assert es_palindromo("Anita lava la tina") is True 
 

def test_es_palindromo_false():
    assert es_palindromo("hola") is False 
 

def test_capitalizar_palabras():
    assert capitalizar_palabras("hola mundo") == "Hola Mundo"
    assert capitalizar_palabras("python es genial") == "Python Es Genial" 
 

def test_contar_vocales():
    assert contar_vocales("hola mundo") == 4
    assert contar_vocales("AEIOU") == 5 
 

def test_caesar_cipher():
    assert caesar_cipher("abc", 1) == "bcd"
    assert caesar_cipher("xyz", 1) == "yza"
    assert caesar_cipher("ABC", 2) == "CDE"
    assert caesar_cipher("Hola, mundo!", 3) == "Krod, pxqgr!"


Necesito que los llamados de las funciones sean los siguientes:

def es_palindromo(texto: str) -> bool:

def capitalizar_palabras(texto: str) -> str:

def contar_vocales(texto: str) -> int:

def caesar_cipher(texto: str, desplazamiento: int) -> str:


**Resultado obtenido**:
def es_palindromo(texto: str) -> bool:
    texto_normalizado = ""

    for caracter in texto.lower():
        if caracter.isalnum():
            texto_normalizado += caracter

    return texto_normalizado == texto_normalizado[::-1]


def capitalizar_palabras(texto: str) -> str:
    palabras = texto.split()
    resultado = []

    for palabra in palabras:
        if palabra:
            palabra_capitalizada = palabra[0].upper() + palabra[1:].lower()
            resultado.append(palabra_capitalizada)

    return " ".join(resultado)


def contar_vocales(texto: str) -> int:
    vocales = "aeiou"
    contador = 0

    for caracter in texto.lower():
        if caracter in vocales:
            contador += 1

    return contador


def caesar_cipher(texto: str, desplazamiento: int) -> str:
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


**¿Lo usaste tal cual o lo modificaste?**
Es identico al prompt 1 salvo por el test, pero de ahora en adelante indico como deben estar estructurados los llamados para evitar corregirlos como en el ejercicio 3 "listas.py"

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts? 
> Aprendí que trabajar con prompts conlleva un esfuerzo que requiere de capacidad para mantener la concentración y la atención para realizar una tarea probablemente repetitiva durante horas. En mi caso, lo más complicado de este trabajo fueron los preparativos para diseñar el prompt que iba a usar durante todo el trabajo y comprobar que lo que generó la IA era correcto y aprobaba los tests.
- ¿En qué casos la IA fue útil y en cuáles no? 
> La IA me fue utíl en todos los casos / ejercicios. Aunque podría decirse que la IA no me podía ayudar a importar un interprete en PyCharm o como importar los archivos para los tests porque yo no quería gastar tokens innecesariamente, esa decisión me llevo a investigar esa información por mi cuenta.
- ¿Qué harías diferente la próxima vez?
> No fue necesario esta vez, pero yo debería averiguar que IAs son las más optimas para este tipo de tareas y tener en cuenta alternativas a ChatGPT cuando se acaben los tokens.
