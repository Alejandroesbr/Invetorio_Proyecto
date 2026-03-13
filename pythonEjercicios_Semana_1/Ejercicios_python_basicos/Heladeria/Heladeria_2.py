
totalClientes = 0
totalVendido = 0
cant_conos = 0
cant_vasos = 0
cant_bananas = 0

precio_cono = 3000
precio_vaso = 4000
precio_bananaSplit = 9000

while True:
    print("\nBienvenido a la heladeria")
    print("MENU\n1.Cono\n2.Vaso\n3.Banana Split\n4.Salir")
    
    opcion = input("\nQue opcion elige: ").lower()

    if opcion == "4" or opcion == "salir":
        print("\n--- RESULTADOS ---")
        print(f"Total Vendido: ${totalVendido}")
        print(f"Total de clientes: {totalClientes}")

        if cant_conos > cant_vasos and cant_conos > cant_bananas:
            mas_vendido = "Cono"
        elif cant_vasos > cant_conos and cant_vasos > cant_bananas:
            mas_vendido = "Vaso"
        elif cant_bananas > cant_conos and cant_bananas > cant_vasos:
            mas_vendido = "Banana Split"
        else:
            mas_vendido = "Empate o sin ventas"
        
        print(f"Producto más vendido: {mas_vendido}")
        break

    cantidad = int(input("Cuantos helados quiere llevar: "))

    if opcion == "1" or opcion == "cono":
        subtotal = precio_cono * cantidad
        cant_conos += cantidad
        totalVendido += subtotal
        totalClientes += 1
        print(f"Total a pagar: ${subtotal}")

    elif opcion == "2" or opcion == "vaso":
        subtotal = precio_vaso * cantidad
        cant_vasos += cantidad
        totalVendido += subtotal
        totalClientes += 1
        print(f"Total a pagar: ${subtotal}")

    elif opcion == "3" or opcion == "banana split":
        subtotal = precio_bananaSplit * cantidad
        cant_bananas += cantidad
        totalVendido += subtotal
        totalClientes += 1
        print(f"Total a pagar: ${subtotal}")

    else:
        print("Opción inválida.")



