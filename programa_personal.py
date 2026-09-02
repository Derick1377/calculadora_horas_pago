TASA_DESCUENTO = 0.05

nombre = input("Escribe tu nombre: ")
horas_trabajadas = float(input("Escribe las horas trabajadas: "))
pago_por_hora = float(input("Escribe cuanto cobras por hora: "))

pago_bruto = horas_trabajadas * pago_por_hora
descuento = pago_bruto * TASA_DESCUENTO
pago_final = pago_bruto - descuento

print("\n--- Resultado ---")
print("Empleado:", nombre)
print("Pago bruto: $", round(pago_bruto, 2))
print("Descuento: $", round(descuento, 2))
print("Pago final: $", round(pago_final, 2))
