from random import randint

vida_pikachu = 80
vida_squirtle = 90

while vida_pikachu > 0 and vida_squirtle > 0:
    # continua el combate

    #turno pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #Bola voltio
        print("Pikachu ha usado: ¡BOLA VOLTIO!")
        vida_squirtle -= 10
    else:
        print("")
