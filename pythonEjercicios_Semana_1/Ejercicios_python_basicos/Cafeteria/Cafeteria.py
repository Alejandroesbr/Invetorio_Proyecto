cafe = 4000
te = 3500
jugo = 5000

print("Bienvenido a la cafeteria, por favor seleccione su bebida y cantidad")
print("1. Cafe")
print("2. Te")
print("3. Jugo")

opcion = input("Que bebido elegiste: ")
cantidad = int(input("Ingrese la cantidad: "))

if opcion == "1" or opcion == "cafe":
    total = cafe * cantidad
    print(f"El total a pagar por {cantidad} cafe(s) es: ${total}")
elif opcion == "2" or opcion == "te":
    total = te * cantidad
    print(f"El total a pagar por {cantidad} te(s) es: ${total}")
elif opcion == "3" or opcion == "jugo":
    total = jugo * cantidad
    print(f"El total a pagar por {cantidad} jugo(s) es: ${total}")
else:    print("Opción no válida. Por favor, seleccione una bebida válida.")