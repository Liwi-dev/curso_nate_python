""" libras a euros """


dolar_euro = 0.94
libras_euros = 1.1340



opcion = input("Que desea hace?\n"
               "A - Convertir de dolar a euro\n"
               "B - Convertir de euro a dolar\n"
               "C - Convertir de libra a euro\n"
               "D - Convertir de euro a libra\n")

text_user = "Introduzca la cantidad {} a convertir: "

if opcion == "A":
    cantidad_de_dinero = float(input(text_user.format("dolares")))
    print("la cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))

if opcion == "B":
    cantidad_de_dinero = float(input(text_user.format("dolares")))
    print("la cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))

if opcion == "C":
    cantidad_de_dinero = float(input(text_user.format("dolares")))
    print("la cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))

if opcion == "D":
    cantidad_de_dinero = float(input(text_user.format("dolares")))
    print("la cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))