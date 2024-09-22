def calcular_descuento(monto_total, porcentaje_descuento=10):
  """
  Calcula el descuento de una compra.

  Args:
    monto_total: El monto total de la compra.
    porcentaje_descuento: El porcentaje de descuento a aplicar. Por defecto es 10%.

  Returns:
    El monto del descuento.
  """

  descuento = monto_total * (porcentaje_descuento / 100)
  return descuento

# Llamadas a la función

# Primer llamada: Usando el valor predeterminado del descuento
monto_total1 = 100
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1
print("Descuento (10%):", descuento1)
print("Monto final:", monto_final1)

# Segunda llamada: Especificando un porcentaje de descuento diferente
monto_total2 = 200
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2
print("\nDescuento (15%):", descuento2)
print("Monto final:", monto_final2)