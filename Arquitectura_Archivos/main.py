# --- DOCUMENTACIÓN Y ESTRUCTURA ---
from servicios import Inventario
import archivos

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
        print("3. Buscar producto")
        print("4. Actualizar inventario")
        print("5. Mostrar estadísticas")
        print("6. Eliminar un producto")
        print("7. Cargar CSV")
        print("8. Guardar CSV")
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
                datos = archivos.cargar_csv_completo()
                if datos:
                    mi_inventario.productos = datos 
                    print("Carga exitosa.")

            case "8":
                archivos.guardar_csv_completo(mi_inventario.productos)


            case "9":
                print("Saliendo del sistema...")
                break

            case _:
                # Manejo de opciones inválidas
                print("Error: Opción no válida, intenta de nuevo.")

# Ejecución del programa
ejecutarMenu()


