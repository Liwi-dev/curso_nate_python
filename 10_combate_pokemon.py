from random import randint

vida_total_pikachu = 80
vida_total_squirtle = 90
tamano_barra = 20


vida_pikachu = vida_total_pikachu
vida_squirtle = vida_total_squirtle


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


    barra_vida = "#" * int(vida_pikachu / vida_total_pikachu * tamano_barra)
    barra_vida = "#" * int(vida_squirtle / vida_total_squirtle * tamano_barra)
    falta_vida = "" * (tamano_barra - len(barra_vida))
    print("{}:  [{}{}] {}/{}".format("Pikachu", barra_vida, falta_vida, vida_pikachu, vida_total_pikachu))
    print("{}: [{}{}] {}/{}".format("Squirtle", barra_vida, falta_vida, vida_squirtle, vida_total_squirtle))
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

    barra_vida = "#" * int(vida_pikachu / vida_total_pikachu * tamano_barra)
    barra_vida = "#" * int(vida_squirtle / vida_total_squirtle * tamano_barra)
    falta_vida = "-" * (tamano_barra - len(barra_vida))
    print("{}: [{}{}] {}/{}".format("Pikachu", barra_vida, falta_vida, vida_pikachu, vida_total_pikachu))
    print("{}: [{}{}] {}/{}".format("Squirtle", barra_vida, falta_vida, vida_squirtle, vida_total_squirtle))
    input("Enter para continuar...""\n\n")


if vida_pikachu > vida_squirtle:
    print("¡Ha ganado Pikachu!")
else:
    print("¡Ha ganado Squirtle!")

