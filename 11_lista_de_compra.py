lista_compra = []

opcion = None


while opcion != "Q":
    opcion = input("¿Que desea comprar? [(Q) para salir]\n")
    if opcion == "Q":
        print("la lista de compras es: {}".format(lista_compra))
        break

    elif opcion not in lista_compra:
        lista_compra.append(opcion)
        opcion = input("Estas seguro que lo quieres añadir? (S)Si/(N)No\n")
        if opcion == "S":
            print("Se ha añadido {} a la lista".format(lista_compra[-1]))
        elif opcion == "N":
            print("No añadimos {} a la lista".format(lista_compra[-1]))
            lista_compra.pop(-1)
    elif opcion in lista_compra:
        print("{} ya esta en la lista!".format(str(lista_compra)))
