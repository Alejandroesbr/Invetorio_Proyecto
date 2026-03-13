
limite = 8
vehiculos_procesados = 0
total_recaudado = 0
cant_carros = 0
cant_motos = 0
pago_maximo = 0
placa_maxima = ""

print(f"--- REGISTRO DE {limite} VEHÍCULOS ---")

while vehiculos_procesados < limite:
    print(f"\nVehículo N° {vehiculos_procesados + 1}")
    placa = input("Ingrese la placa: ")
    tipo = input("Tipo (1. Carro / 2. Moto): ")
    horas = int(input("Horas parqueado: "))

    if tipo == "1" or tipo.lower() == "carro":
        pago_actual = horas * 4000
        cant_carros += 1
    elif tipo == "2" or tipo.lower() == "moto":
        pago_actual = horas * 2000
        cant_motos += 1
    else:
        print("Opción no válida. Intente de nuevo.")
        continue

    total_recaudado += pago_actual

    if pago_actual > pago_maximo:
        pago_maximo = pago_actual
        placa_maxima = placa

    vehiculos_procesados += 1
    print(f"Cobro para {placa}: ${pago_actual}")

print("REPORTE FINAL DEL PARQUEADERO")
print(f"Total recaudado: ${total_recaudado}")
print(f"Carros ingresados: {cant_carros}")
print(f"Motos ingresadas: {cant_motos}")
print(f"El vehículo que más pagó fue {placa_maxima} con ${pago_maximo}")
