"""
# numeros usuario

numeros = [1, 2, 3, 4, 5, 6]

# output
numero_mas_pequeno = 1
numero_mas_grande = 6

"""
print("Agregando numeros a una lista")
"""
numeros = []
usuario = None

for numero in:
    usuario = int(input("¿Que numero quieres agregar? ([Q] para salir): "))
    if usuario == "Q":
        print("Tu numero mas pequeño es: {}".format(min(numeros)))
        print("TGu numero mas grande es: {}".format(max(numeros)))
        break
    elif usuario in numeros:
        print("{} ya esta en la lista".format(usuario))
    elif input("¿Seguro quiere añadir {} a la lista? [si]/[no] ".format(usuario)) == "si":
        numeros.append(usuario)
"""

