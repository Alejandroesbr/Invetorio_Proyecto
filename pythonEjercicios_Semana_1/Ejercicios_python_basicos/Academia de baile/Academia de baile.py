asistencias = int(input("Ingrese la cantidad de asistencias del cliente: "))

asistencia_baja = asistencias <= 5
asistencia_media = asistencias <= 8
asistencia_alta = asistencias >= 9

if asistencia_baja:
    print("El cliente tiene las asistencias bajas.")
elif asistencia_media:
    print("El cliente tiene las asistencias medias.")
elif asistencia_alta:
    print("El cliente tiene las asistencias altas.")