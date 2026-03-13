vainilla = 0
chocolate = 0
fresa = 0

for sabor in ["vainilla", "chocolate", "fresa"]:
    sabor = input("Ingrese el sabor del helado (vainilla, chocolate, fresa) o 'salir' para terminar: ").lower()

    if sabor == "vainilla":
        vainilla += 1
    elif sabor == "chocolate":
        chocolate += 1
    elif sabor == "fresa":
        fresa += 1
    elif sabor == "salir":
        break
    else:
        print("Sabor no reconocido. Por favor, ingrese un sabor válido.")

print(f"Cantidad de helados vendidos por sabor:")
print(f"Vainilla: {vainilla}")
print(f"Chocolate: {chocolate}")
print(f"Fresa: {fresa}")    