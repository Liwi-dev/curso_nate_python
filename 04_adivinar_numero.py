"""
1.el usuario debe adivinar un numero de una secuencia de 1 a 10 dentro de una variable
2 preguntar al usuario cual es el numero de adivinanza
3. si el numero coincide, lo felicitamos
"""
import random

print("Advinina un numero de 1 a 10")
print("¡Comencemos!")

numero_usuario = int(input("En que numero estoy pensando?: "))
mi_numero = random.randint(1, 10)

if numero_usuario == mi_numero:
    print("Felicidades, Ganaste!")
else:
    print("El numero ganador era {}".format(mi_numero))

if numero_usuario > 10:
    print("Te has pasado un poco... es entre 1 y 10")

if numero_usuario < 1:
    print("Te quedaste corto!")

if numero_usuario == 666:
    print("Tambien me gusta Iron Maiden! :)")
