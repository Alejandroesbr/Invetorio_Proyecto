# --- DOCUMENTACIÓN Y ESTRUCTURA ---
from servicios import Inventario
from archivos import GestorInventario

# Función de validación 
def leer_numero(mensaje, tipo=int):
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print("Error: Por favor, ingresa un valor numérico válido.")

def ejecutarMenu():
    mi_inventario = Inventario()
    gestor = GestorInventario(mi_inventario.productos)
    ruta_archivo = "Invetorio_Proyecto/src/inventario.csv"


    # Bucle while para mantener el programa activo 
    while True: 
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar un producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar inventario")
        print("5. Mostrar estadísticas")
        print("6. Eliminar un producto")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input("Ingrese su elección: ")

        # Control de flujo con match
        match opcion:
            case "1":
                print("\nIngrese la información del producto:")
                nombre = input("Nombre: ")
                precio = leer_numero("Precio: ", float)
                cantidad = leer_numero("Cantidad: ", int)
                mi_inventario.agregar_producto(nombre, precio, cantidad)

            case "2":
                # Recorre la lista con un bucle for 
                mi_inventario.mostrar_inventario()

            case "3":
                nombre_buscar = input("¿Qué producto deseas buscar?: ")
                mi_inventario.buscar_producto(nombre_buscar)

            case "4":
                nombre_buscar = input("¿Qué producto deseas actualizar?: ")
                mi_inventario.actualizar_stock(nombre_buscar)

            case "5":
                # Calcula sumatorias de valor y unidades 
                mi_inventario.calcular_estadistica() 

            case "6":
                nombre_borrar = input("Nombre del producto a eliminar: ")
                mi_inventario.eliminar_producto(nombre_borrar)

            case "7":
                # Sincronizamos el inventario del gestor antes de guardar
                gestor.inventario = mi_inventario.productos 
                gestor.guardar_csv(ruta_archivo)

            case "8":
                # Usamos gestionar_carga para aprovechar la lógica de fusión/sobrescribir
                # Pasamos el inventario actual para que el gestor lo actualice
                gestor.inventario = mi_inventario.productos
                gestor.gestionar_carga(ruta_archivo)
                # Actualizamos la lista original con el resultado del gestor
                mi_inventario.productos = gestor.inventario 

            case "9":
                print("Saliendo del sistema...")
                break

            case _:
                # Manejo de opciones inválidas
                print("Error: Opción no válida, intenta de nuevo.")

# Ejecución del programa
ejecutarMenu() 


