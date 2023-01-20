import random

titulo = "El laberinto Mágico"
print("\n" + titulo + "\n" + "·" * len(titulo) + "\n"
"Había una vez un guerrero llamado Rafael que estaba atrapado en un laberinto mágico.Cada vez que tomaba un camino,""\n"
"se encontraba con una nueva bifurcación.Rafael tenía que tomar decisiones rápidas para avanzar a través del""\n"
"laberinto y derrotar al dragón final que guardaba el tesoro.""\n""\n"
"En uno de los primeros caminos, Rafael se encontró con una bifurcación que lo llevaba a la derecha o a la izquierda.""\n")

opcion = input("[OPCION (A) - Camino de la izquierda | OPCION (B) - Camino de la derecha]:""\n")

if opcion == "A":  # Se fue a la izquierda

    print("Después de pensar por un momento,Rafael fue por el camino de la izquierda y se encontró""\n"
          "con otra bifurcación que lo llevaba hacia arriba o hacia abajo.")

    opcion = input("[OPCION (A) - Camino hacia arriba | OPCION (B) - Camino abajo]:""\n")

    if opcion == "A":  # se fue hacia arriba

        print(
            "Esta vez, Rafael decidió ir hacia arriba y se encontró con una puerta secreta que lo llevó a un atajo""\n"
            "hacia el final del laberinto. Rafael agradeció su buena suerte y salio sano y salvo.""\n""FIN""\n")
        exit()
    else:  # se fue hacia abajo

        print("HAS MUERTO QUEMADO POR LA LAVA")
        exit()
else:  # eligio el camino de la derecha

    print("Después de pensar por un momento, Rafael decidió ir a la derecha y se encontró con una trampa de arañas.""\n"
          "Tuvo que decidir si luchar contra las arañas o perder un valioso tiempo y energía rodeando el area.""\n")

    opcion = input("[OPCION (A) - Lucha contra las arañas | OPCION (B) - Rodea el area]:""\n")
    if opcion == "A":  # Lucha contra las arañas
        print("Tuvo que luchar contra las arañas y perdió la vida""\n")
        print("HAS MUERTO DEVORADO POR LAS ARAÑAS")
        exit()
    else:  # DIO UN RODEO
        print("Rafael acabó de una pieza pero perdio mucha energia dando el rodeo""\n")
    print("Continuó avanzando por el camino de la derecha y pronto llegó a una sala llena de tesoros.""\n"
          "Allí encontró una espada mágica con poderosos encantamientos. Rafael tuvo que tomar una decisión rápida:""\n"
          )
    opcion = input("[OPCION (A) - Coge la espada | OPCION (B) - Continua sin ella]:""\n")
    espada_en_inventario = False  # LA ESPADA NO ESTA EN EL INVENTARIO POR AHORA

    if opcion == "A":  # COGE LA ESPADA
        print("Coges la espada")
        espada_en_inventario = True
    elif opcion == "B":  # NO COGE LA ESPADA
        print("Continuas sin ella")
        espada_en_inventario = False
    else:
        print("HAS MUERTO APLASTADO POR UNA AVALANCHA DE MONEDAS DE ORO")

    numero_fauno = random.randint(1, 50)
    print("Mientras avanzaba por el laberinto, Rafael se encontró con un fauno que le hizo resolver un acertijo""\n"
          "matemático. Rafael tuvo que adivinar el resultado de sumar {} + 25.".format(numero_fauno))
    opcion = int(input("¿Cual es el resultado? "))

    pocion = False
    if opcion == 25 + numero_fauno:  # ACIERTA
        print("Rafael pensó cuidadosamente y finalmente dio con la respuesta correcta. El fauno le dio una""\n"
              "poción mágica como recompensa.")
        print("Pocion Mágica Añadida al Inventario")
        pocion = True
    else:  # NO ACIERTA
        print("HAS MUERTO ENVENENADO POR EL FAUNO")
    print("Finalmente, Rafael llegó al final del laberinto y se encuentra al dragón.""\n")

    opcion = input("[OPCION (A) - Te haces bola | OPCION (B) - Te enfrentas al dragon]:")

    if opcion == "A":  # NO SE ENFRENTA AL DRAGON
        print("El dragon te mira desconcertado y te calcina con una bola de fuego""\n""HAS MUERTO CALCINADO")
    elif opcion == "B" and espada_en_inventario == True and pocion == True:  # TIENESTODO
        print("Rafael llegó al final del laberinto y se enfrentó al dragón. La espada y la poción mágica le dieron""\n"
              "una ventaja en la batalla y Rafael logró derrotar al dragón y obtener el tesoro. Rafael agradeció su""\n"
              "determinación y su habilidad para superar los obstáculos del camino de la derecha, así como su""\n"
              "inteligencia al resolver el acertijo matemático y encontrar la espada mágica. Salió del laberinto""\n"
              "con una gran cantidad de tesoros y una valiosa lección aprendida.""\n")
    elif opcion == "B" and espada_en_inventario == False and pocion == True:  # TE FALTA LA ESPADA
        print("Mueres humillado por el dragon por ir a luchar con el a puños""\n""HAS MUERTO HUMILLADO")
    else:  # NO HACES NADA
        print("Mueres de hambre por no haber sabido que hacer""\n""MUERES DE HAMBRE")
