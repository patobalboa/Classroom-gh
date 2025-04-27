# Desarrollo de Algoritmos - Introducción a Python

## 1. ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, fácil de aprender y ampliamente utilizado. Es ideal para principiantes porque su sintaxis es simple y legible. Con Python, puedes crear desde programas básicos hasta aplicaciones complejas.

---

## 2. Variables en Python

Una variable es un espacio en memoria donde se almacena un valor. En Python, no necesitas declarar el tipo de dato, simplemente asignas un valor.

**Ejemplo:**

```python
nombre = "Juan"
edad = 25
```

---

## 3. Tipos de datos básicos

| Tipo    | Descripción                       | Ejemplo         |
| ------- | --------------------------------- | --------------- |
| `int`   | Números enteros                   | `10`, `-5`      |
| `float` | Números decimales                 | `3.14`, `-0.01` |
| `str`   | Cadenas de texto                  | `"Hola"`, `'A'` |
| `bool`  | Valores lógicos (verdadero/falso) | `True`, `False` |

---

## 4. Entrada y salida de datos

### Mostrar mensajes con `print()`

```python
print("Hola, bienvenido al curso")
```

### Solicitar datos con `input()`

```python
nombre = input("¿Cómo te llamas? ")
```

### Concatenación de texto

**Método 1: Uso de `+`**

```python
print("Hola, " + nombre)
```

**Importante:**  La concatenación solo funciona con cadenas. Si intentas concatenar un número, debes convertirlo a cadena usando `str()`.


```python
edad = 25
print("Tienes " + str(edad) + " años")
```


**Método 2: Uso de `f-strings`**

f-strings son una forma moderna y eficiente de formatear cadenas. Permiten insertar variables directamente en la cadena sin necesidad de convertirlas a cadena manualmente.

```python
nombre = "Juan"
edad = 25
# Para usar f-strings, debes colocar una `f` antes de la cadena y usar llaves `{}` para insertar variables.
print(f"Hola, {nombre}. Tienes {edad} años")
```


---

## 5. Operadores Matemáticos

| Operador | Descripción      | Ejemplo  | Resultado |
| -------- | ---------------- | -------- | --------- |
| `+`      | Suma             | `5 + 3`  | `8`       |
| `-`      | Resta            | `10 - 4` | `6`       |
| `*`      | Multiplicación   | `2 * 3`  | `6`       |
| `/`      | División         | `10 / 2` | `5.0`     |
| `%`      | Módulo (residuo) | `10 % 3` | `1`       |
| `**`     | Potencia         | `2 ** 3` | `8`       |

---

## 6. Operadores Comparativos

| Operador | Descripción       | Ejemplo  | Resultado |
| -------- | ----------------- | -------- | --------- |
| `==`     | Igual a           | `5 == 5` | `True`    |
| `!=`     | Distinto de       | `5 != 3` | `True`    |
| `>`      | Mayor que         | `5 > 3`  | `True`    |
| `<`      | Menor que         | `3 < 5`  | `True`    |
| `>=`     | Mayor o igual que | `5 >= 5` | `True`    |
| `<=`     | Menor o igual que | `3 <= 5` | `True`    |

**Ejemplo en condicionales:**

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

---

## 7. Condicionales (`if`, `elif`, `else`)

Los condicionales permiten ejecutar código dependiendo de una condición.

**Ejemplo:**

```python
nota = 7.0
if nota >= 6.0:
    print("Excelente")
elif nota >= 4.0:
    print("Aprobado")
else:
    print("Reprobado")
```

---

## 8. Buenas prácticas al escribir código

- Usa nombres descriptivos para las variables:
  ```python
  edad = 25
  ```
- Usa `snake_case` para nombres de variables que contienen varias palabras:
  ```python
  nombre_completo = "Juan Pérez"
  ```
- Escribe comentarios útiles:
  ```python
  # Calcula el año de nacimiento
  ```
- Indenta correctamente (usa 4 espacios):
  ```python
  if edad >= 18:
      print("Eres mayor de edad")
  ```
  


---

## 9. Tipos de errores comunes en Python

| Error               | Descripción                                   |
| ------------------- | --------------------------------------------- |
| `SyntaxError`       | Error de sintaxis, como paréntesis faltantes. |
| `IndentationError`  | Error de indentación (espacios incorrectos).  |
| `NameError`         | Uso de una variable no definida.              |
| `TypeError`         | Operación entre tipos incompatibles.          |
| `ValueError`        | Valor inválido para una operación.            |
| `ZeroDivisionError` | División entre cero.                          |

---

## 10. Como ejecutar un programa en Python en VSCode

1. Abre la terminal integrada en VSCode (`Menu > Terminal > Nueva Terminal`).

2. En la terminal que se abre, para ejecutar identificamos el archivo que queremos ejecutar. Por ejemplo, si el archivo se llama `mi_programa.py`, escribimos:

   ```bash
   python mi_programa.py
   ```

   - Si estás en Windows y tienes Python 3 instalado, puedes usar `py` en lugar de `python`:

   ```bash
   py mi_programa.py
   ```
   - Si el archivo está en una carpeta diferente, asegúrate de navegar a esa carpeta primero usando el comando `cd` (cambiar directorio). Por ejemplo:

   ```bash
   cd ruta/a/mi/carpeta
   python mi_programa.py
    ```

3. Presiona `Enter` y observa la salida en la terminal.

## 11. Actividad Práctica

Escribe un programa que:

1. Solicite el nombre y la edad del usuario.
2. Calcule el año de nacimiento.
3. Indique si el usuario es mayor o menor de edad.
4. Incluya comentarios y aplique operadores matemáticos.

**Ejemplo de solución:**

```python
# Solicitar datos al usuario
nombre = input("¿Cómo te llamas? ")

edad = int(input("¿Cuántos años tienes? "))

# Calcular el año de nacimiento
anio_actual = 2025
anio_nacimiento = anio_actual - edad

# Determinar si es mayor o menor de edad
if edad >= 18:
    print(f"Hola, {nombre}. Naciste en {anio_nacimiento} y eres mayor de edad.")
else:
    print(f"Hola, {nombre}. Naciste en {anio_nacimiento} y eres menor de edad.")
```

---

## 12. Recursos adicionales

- [Documentación oficial de Python](https://docs.python.org/3/)
- [Tutoriales de Python en W3Schools](https://www.w3schools.com/python/)
- [Curso Python - HolaMundo (YouTube Video)](https://youtu.be/tQZy0U8s9LY?si=YVLLWzhyM0Lthjl8)


