import csv

class GestorInventario:
    def __init__(self):
        self.inventario = []

    def guardar_csv(self, ruta, incluir_header=True):
        try:
            if not self.inventario:
                print("Inventario vacío.")
                return
            
            with open(ruta, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                
                if incluir_header:
                    writer.writerow(['nombre', 'precio', 'cantidad'])

                for producto in self.inventario:
                    writer.writerow([producto['nombre'], producto['precio'], producto['cantidad']])
            
            print(f"Inventario guardado en {ruta}")
        except PermissionError:
            print("Error: Archivo bloqueado o sin permisos.")

    def cargar_csv(self, ruta):
        productos_validos = []
        errores = 0
        
        try:
            with open(ruta, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                # Validar encabezados
                if reader.fieldnames != ['nombre', 'precio', 'cantidad']:
                    print("Error: Encabezado inválido (debe ser: nombre,precio,cantidad).")
                    return None

                for fila in reader:
                    try:
                        # Validar datos básicos
                        if not all(fila.values()): raise ValueError
                        
                        nombre = fila['nombre'].strip()
                        precio = float(fila['precio'])
                        cantidad = int(fila['cantidad'])

                        if precio < 0 or cantidad < 0: raise ValueError
                        
                        productos_validos.append({
                            'nombre': nombre, 'precio': precio, 'cantidad': cantidad
                        })
                    except (ValueError, TypeError, KeyError):
                        errores += 1

            if errores > 0:
                print(f"Aviso: {errores} fila(s) inválida(s) omitida(s).")
            return productos_validos

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta}.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        return None

    def gestionar_carga(self, ruta):
        nuevos_productos = self.cargar_csv(ruta)
        if nuevos_productos is None:
            return

        opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
        
        if opcion == 'S':
            self.inventario = nuevos_productos
            print(f"Resumen: Se reemplazó el inventario con {len(nuevos_productos)} productos.")
        else:
            # Lógica de Fusión
            for nuevo in nuevos_productos:
                encontrado = False
                for actual in self.inventario:
                    if actual['nombre'].lower() == nuevo['nombre'].lower():
                        actual['cantidad'] += nuevo['cantidad']
                        actual['precio'] = nuevo['precio']
                        encontrado = True
                        break
                if not encontrado:
                    self.inventario.append(nuevo)
            print(f"Resumen: Fusión completada.")
