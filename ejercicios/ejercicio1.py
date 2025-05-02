# Ejercicio 1: Calculadora simple

# Instrucciones:
# - Pedir al usuario el primer número.
# - Pedir al usuario el segundo número.
# - Preguntar qué operación desea realizar (+, -, *, /).
# - Mostrar el resultado con el mensaje: "El resultado es: "

# Tu código aquí:

# Solicitar el primer número:
n1 = int(input("Introduce el primer número: "))
# Solicitar el segundo número:
n2 = int(input("Introduce el segundo número: "))
# Pedir la operación a realizar:
operacion = input("¿Qué operación deseas realizar (+, -, *, /)? ")

# Calcular el resultado según la operación:

if operacion == '+':
    resultado = n1 + n2
elif operacion == '-':
    resultado = n1 - n2
elif operacion == '*':
    resultado = n1 * n2
elif operacion == '/':
    resultado = n1 / n2
else:
    resultado = "Operación no válida"

# Mostrar el resultado:
print("El resultado es:", resultado)
