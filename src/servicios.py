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

    def buscar_producto(self, nombre):
        # BÚSQUEDA DE PRODUCTOS:
        # Recorre la lista para encontrar una coincidencia exacta por nombre.
        # Retorna el diccionario del producto si existe, o None si no.
        nombre_buscado = nombre.strip().lower()
        for p in self.productos:
            if p["nombre"].lower() == nombre_buscado:
                print(f"\nProducto encontrado: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['cantidad']}")
                return p  # Retorna el diccionario encontrado
        
        print(f"El producto '{nombre}' no existe en el inventario.")
        return None


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

    def calcular_estadistica(self):
        if not self.productos:
            print("No hay productos para calcular estadísticas.")
            return

        # Definimos la lambda para el subtotal (precio * cantidad)
        calcular_subtotal = lambda p: p["precio"] * p["cantidad"]

        # Inicializamos con el primer producto para comparar
        p_mas_caro = self.productos[0]
        p_mayor_stock = self.productos[0]
        
        total_valor = 0
        total_unidades = 0

        for p in self.productos:
            # Totales
            total_valor += calcular_subtotal(p)
            total_unidades += p["cantidad"]
            
            # Logica para el mas caro
            if p["precio"] > p_mas_caro["precio"]:
                p_mas_caro = p
                
            # Logica para el mayor stock
            if p["cantidad"] > p_mayor_stock["cantidad"]:
                p_mayor_stock = p

        print("ESTADISTICAS DEL INVENTARIO")
        print(f"Valor total en mercancia: ${total_valor:,.2f}")
        print(f"Total de unidades en stock: {total_unidades}")
        print(f"Producto mas caro: {p_mas_caro['nombre']} (${p_mas_caro['precio']})")
        print(f"Mayor existencia: {p_mayor_stock['nombre']} ({p_mayor_stock['cantidad']} unidades)")

