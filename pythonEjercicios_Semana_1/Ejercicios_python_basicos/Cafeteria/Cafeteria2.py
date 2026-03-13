cafe = 4000
capuchino = 7000
pastel = 6000
total_dia = 0 
total = 0

while True:
    print("Bienvenido a la cafeteria, por favor seleccione su bebida y cantidad")
    print("1. Cafe")
    print("2. Capuchino")
    print("3. Pastel")
    print("4. Salir")

    opcion = input("Que bebido elegiste: ")


    if opcion == "4" or opcion == "salir":
        print("\n--- RESULTADOS ---")
        print(f"Total Vendido: ${total_dia}")
        break

    cantidad = int(input("Ingrese la cantidad: "))

    if opcion == "1" or opcion == "cafe":

        compra = cafe * cantidad
        if compra > 20000:
            descuento = compra * 0.10
            total = compra - descuento
            print ("descuento aplicado")
        else:
            print(f"No aplica descuento. Total a pagar: ${compra:.2f}")
        total_dia += total
        print(f"El total a pagar por {cantidad} cafe es: ${total}")

    elif opcion == "2" or opcion == "capuchino":
        compra = capuchino * cantidad
        if compra > 20000:
            descuento = compra * 0.10
            total = compra - descuento
            print ("descuento aplicado")
        else:
            print(f"No aplica descuento. Total a pagar: ${compra:.2f}")
        total_dia += total
        print(f"El total a pagar por {cantidad} capuchino es: ${total}")

    elif opcion == "3" or opcion == "pastel":
        compra = pastel * cantidad
        if compra > 20000:
            descuento = compra * 0.10
            total = compra - descuento
            print ("descuento aplicado")
        else:
            print(f"No aplica descuento. Total a pagar: ${compra:.2f}")
        print(f"El total a pagar por {cantidad} pastel es: ${total}")
        total_dia += total

    else: print("Opción no válida. Por favor, seleccione una bebida válida.")



