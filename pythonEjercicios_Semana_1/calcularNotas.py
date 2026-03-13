def pedir_puntaje(materia):
            while True:
                try:
                    puntaje = float(input(f"Ingrese el puntaje de {materia}: "))
                    if 0 <= puntaje <= 100:
                        print(f"Registrado: {puntaje}\n")
                        return puntaje
                    print("Error: El puntaje debe estar entre 0-100.")
                except ValueError:
                    print("Error: Ingrese un número válido.")

total_estudiantes = 0
suma_promedios = 0
reprobados = 0
regulares = 0
excelentes = 0
mejor_promedio = -1
nombre_mejor_estudiante= ""

nombre_modulo = input("Ingrese el nombre del módulo: ")

while True:

    print(f"\n--- Menú de Evaluación: {nombre_modulo} ---\n")
    print("1. Evaluar un estudiante")
    print("2. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
            
            nombre = input("\nIngrese el nombre del estudiante: ")

            software = pedir_puntaje("Desarrollo de Software")
            ingles = pedir_puntaje("Inglés")
            socioemocional = pedir_puntaje("Habilidades Socioemocionales")

            promedio = (software * 0.6) + (ingles * 0.2) + (socioemocional * 0.2)
            
            if promedio < 50:
                estado = "\033[91m Reprobado\033[0m"
                reprobados += 1
            elif promedio < 80:
                estado = "\033[93m Regular\033[0m"
                regulares += 1
            else:
                estado = "\033[92m Excelente\033[0m"
                excelentes += 1

            print(f"estudiante: {nombre}")
            print(f"Módulo: {nombre_modulo}")
            print(f"Promedio Final: {promedio:.2f}")
            print(f"Clasificación: {estado}")

            if software < 50:
                print("AVISO: Debe reforzar el frente técnico principal.")
            print("-" * 30)

            total_estudiantes += 1
            suma_promedios += promedio

            if promedio > mejor_promedio:
                mejor_promedio = promedio
                nombre_mejor_estudiante = nombre

    elif opcion == "2":
            
            if total_estudiantes > 0:
                promedio_grupal = suma_promedios / total_estudiantes
                print(f"\n=== RESUMEN DEL MÓDULO: {nombre_modulo} ===")
                print(f"Total de estudiantes registrados: {total_estudiantes}")
                print(f"Promedio general del grupo: {promedio_grupal:.2f}")
                print(f"Cantidad de Reprobados: {reprobados}")
                print(f"Cantidad de Regulares: {regulares}")
                print(f"Cantidad de Excelentes: {excelentes}")
                print(f"Mejor desempeño: {nombre_mejor_estudiante} con {mejor_promedio:.2f}")
            else:
                print("\nNo se registraron datos.")
            
            print("\n¡Hasta luego!")
            break 
    else:
            print("Opción inválida. Por favor, intrese 1 o 2.")