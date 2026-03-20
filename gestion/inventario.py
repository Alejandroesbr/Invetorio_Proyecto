class Inventario:
    
    def __init__(self): 
        # INICIALIZACIÓN: Se crea una lista vacía para almacenar los diccionarios de productos.
        self.productos = []
        
    def agregar_producto(self, nombre, precio, cantidad):
        # REGISTRO DE PRODUCTOS: 
        # Crea un diccionario con los datos y lo añade a la lista 'self.productos'.
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.productos.append(producto)
        print(f"{nombre} agregado al inventario.")

    def mostrar_inventario(self):
        # VISUALIZACIÓN DE DATOS:
        # Utiliza un bucle for para recorrer la lista y mostrar cada producto.
        # Valida si el inventario está vacío antes de intentar imprimir.
        print("\n--- INVENTARIO ACTUAL ---")
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for i, p in enumerate(self.productos): 
                # Imprime en el formato solicitado: Producto | Precio | Cantidad
                print(f"{i}. Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")

    def actualizar_stock(self, nombre):
        # GESTIÓN DE ACTUALIZACIONES:
        # Busca un producto específico por nombre y modifica su valor de 'cantidad'.
        # Incluye validación de datos para asegurar que la entrada sea un número.
        producto_encontrado = None
        for p in self.productos:
            if p["nombre"].lower() == nombre.strip().lower():
                producto_encontrado = p
                break
        
        if not producto_encontrado:
            print(f"Error: El producto '{nombre}' no existe.")
            return 
            
        while True:
            try:
                nueva_cant = int(input(f"Nueva cantidad para '{producto_encontrado['nombre']}': "))
                producto_encontrado["cantidad"] = nueva_cant
                print("Stock actualizado.")
                break
            except ValueError:
                print("Error: Introduce un número entero válido.")

    def calcular_estadistica(self):
        # CÁLCULO DE ESTADÍSTICAS:
        # Acumula el valor monetario (precio * cantidad) y el conteo total de unidades.
        total_valor = 0
        total_productos = 0
        
        if not self.productos:
            print("No hay productos para calcular estadísticas.")
            return
            
        for p in self.productos:
            total_valor += p["precio"] * p["cantidad"]
            total_productos += p["cantidad"]
            
        print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
        print(f"Valor total en mercancía: ${total_valor}")
        print(f"Total de unidades en stock: {total_productos}")
        
    def eliminar_producto(self, nombre):
        # ELIMINACIÓN DE REGISTROS:
        # Localiza el diccionario dentro de la lista y lo remueve definitivamente.
        producto_encontrado = None
        for p in self.productos:
            if p["nombre"].lower() == nombre.strip().lower():
                producto_encontrado = p
                break 
                
        if not producto_encontrado:
            print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")
            return
            
        self.productos.remove(producto_encontrado)
        print(f"El producto '{producto_encontrado['nombre']}' ha sido eliminado con éxito.")


