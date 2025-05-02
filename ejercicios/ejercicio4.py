# Ejercicio 4: Mayor de tres números
# Instrucciones:
# - Pedir tres números al usuario.
# - Determinar cuál es el mayor utilizando condicionales (if, elif, else).
# - Mostrar el número mayor con el mensaje: "El número mayor es: ".

# Tu código aquí:

# Pedir el primer número:
n1 = int(input("Introduce el primer número: "))
# Pedir el segundo número:

n2 = int(input("Introduce el segundo número: "))
# Pedir el tercer número:
n3 = int(input("Introduce el tercer número: "))


# Comparar los números para saber cuál es el mayor:
if n1 > n2:
    if n1 > n3:
        mayor = n1
    else:
        mayor = n3
else:
    if n2 > n3:
        mayor = n2
    else:
        mayor = n3

# Mostrar el resultado:
print("El número mayor es:", mayor)
