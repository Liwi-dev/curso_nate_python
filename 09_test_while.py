"""
respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("¿Qué opcion prefieres [A, B, C]?""\n")


if respuesta == "A":
    print("¡Has eligido bien!")
elif respuesta == "B":
    print("¡Podrias haber elegido mejor!")
elif respuesta == "C":
    print("¡Elegiste mal!")
else:
    print("No has dado una respuesta con sentido")
"""

numero = 12

while numero > 1:
    print("Mi numero {} es mayor que 1".format(numero))
    numero -= 1
