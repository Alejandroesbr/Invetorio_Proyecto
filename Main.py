# --- DOCUMENTACIÓN Y ESTRUCTURA ---

from gestion.inventario import Inventario

# Función de validación 
def leer_numero(mensaje, tipo=int):
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingresa un valor numérico válido.")

def ejecutarMenu():
    mi_inventario = Inventario()

    # Bucle while para mantener el programa activo 
    while True: 
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar un producto")
        print("2. Mostrar inventario")
        print("3. Actualizar inventario")
        print("4. Mostrar estadísticas")
        print("5. Eliminar un producto")
        print("6. Salir")

        opcion = input("Ingrese su elección: ")

        # Control de flujo con if/elif/else 
        if opcion == "1":
            print("\nIngrese la información del producto:")
            nombre = input("Nombre: ")
            precio = leer_numero("Precio: ", float)
            cantidad = leer_numero("Cantidad: ", int)
            mi_inventario.agregar_producto(nombre, precio, cantidad)

        elif opcion == "2":
            # Recorre la lista con un bucle for 
            mi_inventario.mostrar_inventario()

        elif opcion == "3":
            nombre_buscar = input("¿Qué producto deseas actualizar?: ")
            mi_inventario.actualizar_stock(nombre_buscar)

        elif opcion == "4":
            # Calcula sumatorias de valor y unidades 
            mi_inventario.calcular_estadistica() 

        elif opcion == "5":
            nombre_borrar = input("Nombre del producto a eliminar: ")
            mi_inventario.eliminar_producto(nombre_borrar)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            # Manejo de opciones inválidas 
            print("Error: Opción no válida, intenta de nuevo.")

# Ejecución del programa
ejecutarMenu()

# Semana 2
# Aplicar estructuras de control (bucles y condicionales) y tipos de datos 
# compuestos (listas y diccionarios) para gestionar colecciones de datos en Python.
