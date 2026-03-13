edad = int(input("Ingrese la edad del cliente: "))

claseJuvenil = edad <= 17
claseGeneral = edad <= 59
claseSenior = edad >= 60

if edad < 13:
    print("Edad no válida. NO puede ingresar al gimnasio.")
elif claseJuvenil:
    print("El cliente pertenece a la clase Juvenil.")
elif claseGeneral:
    print("El cliente pertenece a la clase General.")
elif claseSenior:
    print("El cliente pertenece a la clase Senior.")