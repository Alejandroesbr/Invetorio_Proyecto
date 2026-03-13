bajo_compromiso = 0
medio_compromiso = 0
alto_compromiso = 0

for i in range(1, 6):
    print(f"\n--- Registro Persona {i} ---")
    nombre = input("Nombre: ")
    dias = int(input("Días asistidos en la semana: "))
    minutos = int(input("Minutos promedio por día: "))

    if dias < 3:
        print(f"{nombre} tiene: Bajo compromiso")
        bajo_compromiso += 1
    elif 3 <= dias <= 4:
        print(f"{nombre} tiene: Compromiso medio")
        medio_compromiso += 1
    else:  # 5 o más
        print(f"{nombre} tiene: Compromiso alto")
        alto_compromiso += 1

# 4. Mostrar resultados finales

print("RESUMEN DEL GIMNASIO")
print(f"Bajo compromiso: {bajo_compromiso}")
print(f"Compromiso medio: {medio_compromiso}")
print(f"Compromiso alto: {alto_compromiso}")

