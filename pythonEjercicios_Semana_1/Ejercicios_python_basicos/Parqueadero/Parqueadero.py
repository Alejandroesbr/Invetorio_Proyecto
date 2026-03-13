hora_adicional = 0 
cobro_hora_inicial = 5000
cobro_hora_adicional = 3000

horas = int(input("¿Cuántas horas estuvo el carro en el parqueadero? "))

if horas <= 1:
    total = cobro_hora_inicial
else:
    total = cobro_hora_inicial + (horas * cobro_hora_adicional)

print(f"El total a pagar es: {total} pesos")    