capacidad = int(input("Ingrese la capacidad total de la sala: "))
asientos_ocupados = 0

ninos = 0
adultos = 0
adultos_mayores = 0

while asientos_ocupados < capacidad:
    print(f"\nAsientos disponibles: {capacidad - asientos_ocupados}")
    print("1. Registrar ingreso por edad")
    print("2. Cerrar sala ahora")
    
    opcion = input("Elija una opción (1-2): ")

    if opcion == "2":
        break
    
    if opcion == "1":
        edad = int(input("Ingrese la edad de la persona: "))
        
        # Tu clasificación por edad
        if edad < 13:
            ninos += 1
            clasificacion = "Niño"
        elif edad < 60:
            adultos += 1
            clasificacion = "Adulto"
        else:
            adultos_mayores += 1
            clasificacion = "Adulto mayor"
        
        asientos_ocupados += 1
        print(f"Registrado como: {clasificacion}")
    else:
        print("Opción no válida.")

print(f"Total personas: {asientos_ocupados}")
print(f"• Niños: {ninos}\n• Adultos: {adultos}\n• Adultos mayores: {adultos_mayores}")

if asientos_ocupados == capacidad:
    print("ESTADO: SALA LLENA")
else:
    print(f"ESTADO: Quedaron {capacidad - asientos_ocupados} asientos libres.")
