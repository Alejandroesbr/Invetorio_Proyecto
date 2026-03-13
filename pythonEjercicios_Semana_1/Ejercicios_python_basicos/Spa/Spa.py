while True:

    print ("---Bienvenido al Spa---")
    print ("1.masaje") 
    print ("2.facial") 
    print ("3.manicure") 

    opcion = input("Que servicio le gustaria usar:")
    if opcion == "1" or opcion == "masaje":
        print ("El servicio esta dispobile")
        break

    elif opcion == "2" or opcion == "facial":
        print ("El servicio no esta disponible por el momento")
        break

    elif opcion == "3" or opcion == "manicure":
        print ("El Servicio esta disponible")
        break

    else: print("Opcion no disponible")
