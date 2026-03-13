total_alimento = 0
total_juguete = 0
total_accesorio = 0

ventas_realizadas = 0
limite_ventas = 10

print("--- REGISTRO DE 10 VENTAS - TIENDA DE MASCOTAS ---")

while ventas_realizadas < limite_ventas:
    print(f"\nVenta N° {ventas_realizadas + 1}")
    print("Categorías: 1. Alimento | 2. Juguete | 3. Accesorio")
    
    opcion = input("Seleccione categoría (1-3): ")
    valor = float(input("Ingrese el valor de la compra: "))

    if opcion == "1":
        total_alimento += valor
    elif opcion == "2":
        total_juguete += valor
    elif opcion == "3":
        total_accesorio += valor
    else:
        print("Categoría no válida. Intente de nuevo.")
    ventas_realizadas += 1

if total_alimento > total_juguete and total_alimento > total_accesorio:
    mayor_cat = "Alimento"
    monto_mayor = total_alimento
elif total_juguete > total_accesorio:
    mayor_cat = "Juguete"
    monto_mayor = total_juguete
else:
    mayor_cat = "Accesorio"
    monto_mayor = total_accesorio

print("REPORTE TOTAL DE VENTAS")
print(f"Total Alimento:   ${total_alimento:,.2f}")
print(f"Total Juguete:    ${total_juguete:,.2f}")
print(f"Total Accesorio:  ${total_accesorio:,.2f}")
print(f"La categoría que más generó fue: {mayor_cat} (${monto_mayor:,.2f})")
