ios_android = input("Que te gusta?: ios o android \n")

tienes_dinero = input("Tienes dinero? (si/no) \n")

if ios_android == "android":
    if tienes_dinero == "no":
        print("Comprate un android chino de 100 pavos!")
    elif tienes_dinero == "si":
        camara_movil = input("Te importa la camara del movil? (si/no) \n")
        if camara_movil == "si":
            print("Comprate el Google Pixel 7 Pro!")
        elif camara_movil == "no":
            print("Comprate un android calidad-precio")


if ios_android == "ios":
    if tienes_dinero == "si":
        print("Comprate el iphone 14 Pro Max")
    elif tienes_dinero == "no":
        print("Comprate un iphone de segunda mano")
