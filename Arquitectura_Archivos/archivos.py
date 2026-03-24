import csv
import os

# Configuración de la ruta
ARCHIVO = "/home/Coder/Escritorio/Clan_8/Alejandro_Escobar/proyectoInventario/Arquitectura_Archivos/inventario.csv"

def cargar_csv_completo():
    if not os.path.exists(ARCHIVO):
        print("El archivo no existe.")
        return []
    
    productos = []
    try:
        with open(ARCHIVO, mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                # Convertimos datos a los tipos correctos
                fila['precio'] = float(fila['precio'])
                fila['cantidad'] = int(fila['cantidad'])
                productos.append(fila)
        return productos
    except Exception as e:
        print(f"Error al cargar: {e}")
        return []

def guardar_csv_completo(lista_productos):
    try:
        with open(ARCHIVO, mode='w', encoding='utf-8', newline='') as f:
            campos = ["nombre", "precio", "cantidad"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(lista_productos)
        print(f"Guardado en: {ARCHIVO}")
    except Exception as e:
        print(f"Error al guardar: {e}")
