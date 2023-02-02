"""
Ejemplo nate

texto_usuario = "Hola, me llamo Nate. ¿Tú como te llamas?"

Output esperado
mayusculas = 3

"""
import string


texto_usuario = input("Introduzca su texto: ")
letras_mayusculas = 0


for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1

print("Las letras mayusculas son: {}".format(letras_mayusculas))