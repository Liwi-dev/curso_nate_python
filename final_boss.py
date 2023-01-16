import random

print("Juego de la mazmorra\n"
      "----------------------\n"
      "tu y tu compañero de celda os acabais de escapar de la prision espacial, habeis burlado a los guardias y os\n"
      "dirigis hacia al exterior. Entrais en una mazmorra conterolada por mounstruos alienigenas, uno de los guardias \n"
      "ataca a tu compañero, se lo lleva pero tu pasas desapercibido escondido en las sombras. El guardia se retira, \n"
      "es tu posibilidad de escapar. Hacia donde te diriges?\n"
      "\n"
      "A la izquierda tienes una puerta semiabierta, a la derecha una escotilla en el suelo")

opcion = input("[OPCION (A) - Puerta Semiabierta] | [OPCION (B) - Escotilla en el suelo]: ")

if opcion == "A":
      print("Entras en la puerta semiabierta y otro guardia te descubre, que haces?")
      opcion = input("[OPCION (A) - Te haces el dormido] | [OPCION (B) - Sales corriendo hacia la siguiente puerta]: ")

      if opcion == "A":
            print("El guardia te atrapa, te encierran en una celda de maxima seguridad\nFIN")
      elif opcion == "B":
            print("Despues de esa puerta encuentras una rana mutante que te regala un puñal casero hecho con la pata de"
                  "una mesa, lo aceptas?")
            opcion = input("[OPCION (A] - Si | [OPCION (B) - No]: ")

            if opcion == "A":
                  print("Coges el pincho y avanzas, hay dos pasillos circulares, no ves el final de ninguno de los dos, uno"
                        "esta a la derecha y el otro a la izquierda, cual tomas?")

                  opcion = input("[OPCION (A) - Izquierda] | [OPCION (B) - Derecha] ")

                  if opcion == "A":
                        print("La habitacion se hace cada vez mas oscura, ves tan poco que caes en un agujero en el suelo con"
                              "pinchos, mueres a las 2 horas de forma lenta y dolorosa \nFIN")
                  elif opcion == "B:"
                        print("Encuentras la salida, en la puerta hay aparcado un Ferrari espacial, te montas, es tu dia de"
                              " suerte, las llaves estan puestas, Huyes hacia el horizonte\nFIN")

            elif opcion == "B":
                  print("La rana te devora, mueres en forma rapida, el veneno hace efecto de casi de manera instantanea.\nFIN")
            else:
                  print("No has elegido ninguna opcion, simplemente mueres.")
      else:
            print("No has elegido ninguna opcion, simplemente mueres.")

elif opcion == "B":
      print("Caes en una zona inundada, el agua te llega hasta las rodillas, avanzas durante media hora y finalmente"
            " llegas a una zona abierta, seca y con luz, parecen alcantarillas\nEncuentras un palo largo, parece"
            " algo pesado, pero podria servir, lo coges?")
      opcion = input("[OPCION (A) - SI] | [OPCION (B - NO)]: ")

      palo_en_inventario = False