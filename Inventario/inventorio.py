# Bucle infinito para el menú principal

while True: 
    print("\nBienvenido al Sistema de Gestión de Inventario")
    print("1. Agregar un artículo")
    print("2. Salir")
    opcion = input("Ingrese su elección: ")

    if opcion == '1': # Si agrega un artículo, solicita nombre, precio y cantidad
        nombre = input("Ingrese el nombre: ")

        # Bucle infinito solo para el PRECIO
        
        while True: # Asegura que el usuario ingrese un precio válido
            try: # Maneja errores de entrada no numérica
                precio = float(input("Ingrese el precio: "))
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
                break # Si es correcto, sale del bucle del precio
            except ValueError: # Error para entradas no numéricas
                print("Entrada inválida. Por favor, ingrese un precio numérico.")

        # Bucle infinito solo para la CANTIDAD

        while True: # Asegura que el usuario ingrese una cantidad válida
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                break # Si es correcto, sale del bucle de cantidad
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

        costo_total = precio * cantidad
        print(f"\nAgregado: {nombre} | Total: {costo_total}")

    elif opcion == '2': # Opción para salir del programa
        print("¡Adiós!")
        break
    else: # Manejo de errores para opciones inválidas en el menú
        print("Opción inválida.")

# Este software es un sistema simple de control de inventarios diseñado para el registro efectivo de productos. 
# A través de un menú interactivo, los usuarios pueden ingresar el nombre, precio y cantidad de un artículo. 
# Al confirmar que las entradas numéricas son correctas, calcular el costo total automáticamente y mostrar un resumen detallado en la consola, el sistema garantiza la integridad de los datos. 
# Cuenta con un bucle infinito que permite realizar varios registros hasta que el usuario decida salir.