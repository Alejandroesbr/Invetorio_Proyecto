recomendacion_perro = "DogChow"
recomendacion_gato = "Whiskas"
recomendacion_conejo = "Heno"

print("""Bienvenido a la Tienda de mascotas \nPorfavor elige que mascotas tienes:""")

print("1. perro")
print("2. gato")
print("3. conejo")

opcion = input("Que mascota eligio:")

if opcion == "1" or opcion == "perro":
            print (f"se le recomienda a la mascota consumir: {recomendacion_perro}")
elif opcion == "2" or opcion == "gato":
            print (f"se le recomienda a la mascota consumir: {recomendacion_gato}")
elif opcion == "3" or opcion == "conejo":
            print (f"se le recomienda a la mascota consumir: {recomendacion_conejo}")