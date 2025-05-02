# Ejercicio 5: Descuento en compras
# Instrucciones:
# - Pedir al usuario el monto total de la compra.
# - Si el monto es mayor a $50.000, aplicar un 15% de descuento.
# - Mostrar el monto final a pagar y el descuento aplicado.

# Tu código aquí:

# Pedir el monto total:
monto_total = float(input("Introduce el monto total de la compra: "))

# Verificar si corresponde descuento:
if monto_total > 50000:
    descuento = monto_total * 0.15
else:
    descuento = 0


# Calcular el monto final y el descuento si es necesario:
monto_final = monto_total - descuento


# Mostrar el resultado:
print("El total a pagar es:", monto_final)
print("El descuento aplicado es:", descuento)
