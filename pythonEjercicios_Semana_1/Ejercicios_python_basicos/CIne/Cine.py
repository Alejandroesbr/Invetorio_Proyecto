edad = int(input("Ingrese la edad del cliente: "))

menores = edad <= 12
adultos = edad <= 59
mayores = edad <= 60

precio_menores = 8000
precio_adultos = 12000
precio_mayores = 9000

if menores:
    print(f"La personas menores de 12 deben pagar: {precio_menores}")
elif adultos:
    print(f"La personas menores de 59 deben pagar: {precio_adultos}")
elif mayores:
    print(f"La personas mayores de 60 deben pagar: {precio_mayores}")
    
