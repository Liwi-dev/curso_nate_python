"""
# numero elegido por el usuario: 2, output esperado
2 x 1 = 2
2 x 2 = 2
2 x 3 = 2
2 x 4 = 2
2 x 5 = 2
2 x 6 = 2
2 x 7 = 2
2 x 8 = 2
2 x 9 = 2
2 x 10 = 2
"""
print("Introduce un numero y te dire su tabla de multiplicar\n")
numero_usuario = int(input("Introduzca tu numero: "))

for tabla in range(1, 11):
    multiplicacion = numero_usuario * tabla
    print(numero_usuario, "x", multiplicacion)
