# 📦 Sistema de Inventario en Python

## 🧩 Descripción

Este proyecto es un sistema de gestión de inventario desarrollado en Python. Permite administrar productos mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar), además de ofrecer funcionalidades de búsqueda, estadísticas y persistencia de datos mediante archivos CSV.

El sistema está diseñado de forma modular, aplicando estructuras como listas, diccionarios y funciones para mantener un código organizado y escalable.

---

## ⚙️ Funcionalidades

### 📌 Gestión de productos (CRUD)
- Agregar productos al inventario
- Mostrar todos los productos
- Buscar productos por criterio
- Actualizar información de productos
- Eliminar productos

### 🔍 Búsqueda
- Permite ingresar criterios específicos
- Retorna resultados filtrados

### 📊 Estadísticas
- Cálculo de métricas del inventario
- Visualización de resultados

### 💾 Persistencia (CSV)
- Guardar inventario en archivo CSV
- Cargar inventario desde CSV
- Validación de rutas y archivos
- Opciones al cargar:
  - Sobrescribir inventario
  - Fusionar con inventario actual

---

## 🧠 Flujo del sistema

<p align="center">
  <img src="docs/Producto Inventario Flujo-2026-03-26-181808.png" width="600">
</p>

El sistema funciona a través de un menú principal donde el usuario selecciona la operación a realizar:

1. Mostrar productos  
2. Buscar producto  
3. Agregar producto  
4. Actualizar producto  
5. Eliminar producto  
6. Ver estadísticas  
7. Guardar en CSV  
8. Cargar desde CSV  
9. Salir  

Cada opción dirige a un flujo específico con validaciones y manejo de errores.

---

## 🛠️ Tecnologías utilizadas

- Python
- Estructuras de datos:
  - Listas
  - Diccionarios
  - Tuplas
- Manejo de archivos (CSV)
- Programación modular (funciones)

---

## 📁 Estructura del proyecto (ejemplo)

inventario/
│
├── main.py
├── inventario.py
├── funciones.py
├── utils.py
├── data/
│   └── inventario.csv
└── README.md

---

⸻

⚠️ Validaciones implementadas

	•	Verificación de datos al agregar productos
	•	Validación de rutas de archivos
	•	Validación de archivos CSV
	•	Manejo de errores en entrada de usuario
	•	Confirmación en operaciones críticas (como eliminar o sobrescribir)

⸻

🚀 Posibles mejoras

	•	Interfaz gráfica (Tkinter / Web)
	•	Base de datos (SQLite, PostgreSQL)
	•	API REST
	•	Autenticación de usuarios
	•	Reportes avanzados

⸻

python 3.X