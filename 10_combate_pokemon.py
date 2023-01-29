from random import randint

vida_pikachu = 80
vida_squirtle = 90

while vida_pikachu > 0 and vida_squirtle > 0:
    # continua el combate

    # Turno Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #Bola voltio
        print("Pikachu ha usado: ¡BOLA VOLTIO!")
        vida_squirtle -= 10
    else:
        print("Pikachu ha usado ¡ONDA TRUENO!")
        vida_squirtle -= 11

    print("La vida de Pikachu es: {}, La vida de Squirtle es: {}".format(vida_pikachu, vida_squirtle))
    input("Enter para continuar...""\n\n")


    # Turno Squirtle
    print("Turno de Squirtle")
    ataque_squirtle = None

    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("¿Que ataque quieres realizar? [P]Placaje, [A]Pistola Agua, [B]Burbuja""\n\n")

    if ataque_squirtle == "P":
        vida_pikachu -= 10
        print("Squirtle ha usado ¡PLACAJE!")
    elif ataque_squirtle == "A":
        vida_pikachu -= 12
        print("Squirtle ha usado ¡PISTOLA AGUA!")
    elif ataque_squirtle == "B":
        vida_pikachu -= 9
        print("Squirtle ha usado ¡BURBUJA!")

    print("La vida de Pikachu es: {}, La vida de Squirtle es: {}".format(vida_pikachu, vida_squirtle))
    input("Enter para continuar...""\n\n")


if vida_pikachu > vida_squirtle:
    print("¡Ha ganado Pikachu!")
else:
    print("¡Ha ganado Squirtle!")

