hora = int(input("Introduce la hora de llegada (0-23): "))

if 6 <= hora <= 11:
    print("mañana")
elif 12 <= hora <= 17:
    print("tarde")
elif 18 <= hora <= 22:
    print("noche")
else:
    print("fuera de horario")