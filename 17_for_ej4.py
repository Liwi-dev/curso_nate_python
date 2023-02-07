"""
# numeros usuario

numeros = [1, 2, 3, 4, 5, 6]

# output
numero_mas_pequeno = 1
numero_mas_grande = 6

"""
# Solucion de Nate


numeros_introducidos = input("introduzca los numeros separados por coma: ")  # 1,2,3,4,5,6,7,8,9
numeros_usuario = [int(numero) for numero in numeros_introducidos.split(",")]  # List comprehension #for express
# lo que hace split es separar el string por muchas comas
numero_pequeno = min(numeros_usuario)
numero_grande = max(numeros_usuario)

print("Este es tu numero peuqeño: {}""\n"
      "Este es tu numero grande: {}".format(numero_pequeno, numero_grande))

# mi solucion
"""
print("Agregando numeros a una lista")

numerous_usuario = []
usuario = int(input("¿Que numero quieres agregar? ([Q] para salir): "))
numerous_usuario.append(usuario)

while input("¿Quiere añadir mas numeros? [si]/[no] ") == "si":
    usuario = int(input("Introduzca un numero a la lista: "))
    numerous_usuario.append(usuario)
else:
    print("Tu numero mas pequeño es: {}".format(min(numerous_usuario)))
    print("Tu numero mas grande es: {}".format(max(numerous_usuario)))
"""
