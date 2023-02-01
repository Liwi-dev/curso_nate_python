

lista_compra = []
opcion = None

print("Lista de Compras")

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
        print("¡"+"".join(lista_compra), "ya esta en la lista!")


# solucion de nate
"""

lista_de_nate = list()
input_usuario = None

while True:
    input_usuario = input("¿Que desea comprar? [(Q) para salir]\n")
    if input_usuario == "Q":
        break
    elif input_usuario in lista_de_nate:
        print("{} ya esta en la lista".format(input_usuario))
    else:
        if input("¿Seguro quiere añadir {} a la lista? [S]Si/[N]No".format(input_usuario) == "S":
            lista_de_nate.append(input_usuario)

print("La lista de la compra es:")
print(lista_de_nate)
"""