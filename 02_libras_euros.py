""" libras a euros """


dolar_euro = 0.94
libras_euros = 1.1340
euro_libra = 0.88

opcion = input("Que quieres convertir?: (libra o dolar a euro?)")
opcion_2 = float(input("Cual es el monto de " + opcion + " a convertir: "))

if opcion == "libra":
    conversion_lib = opcion_2 * libras_euros
    print("la conversion es ", conversion_lib, "euros")
elif opcion == "dolar":
    conversion_eur = dolar_euro * opcion_2
    print("la conversion es ", conversion_eur, "euros")
