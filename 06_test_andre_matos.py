titulo = "Bienvenido al test sobre Andre Matos\n"
print("\n" + titulo + "-" * len(titulo) + "\n")

points = 0

option = input("Pregunta 1: Cual es el primer album solista de Andre Matos?\n"
               "A - Holy Land\n"
               "B - Reason\n"
               "C - Time To Be Free\n")

if option == "A":
    points += - 10

elif option == "B":
    points = points - 5

elif option == "C":
    points = points + 25
else:
    print("Solo puedes responder: A, B y C")
    exit()

option = input("Pregunta 2: Quien es la esposa de Andre Matos?\n"
               "A - Amanda Sommerville\n"
               "B - Marina Leite\n"
               "C - Penelope Nova\n")

if option == "A":
    points += - 8

elif option == "B":
    points = points + 25

elif option == "C":
    points = points - 15
else:
    print("Solo puedes responder: A, B y C")
    exit()

option = input("Pregunta 2: Que musica le gusta a Andre Matos?\n"
               "A - Hard Rock\n"
               "B - Rock Progresivo\n"
               "C - Musica Clasica\n")

if option == "A":
    points += - 13

elif option == "B":
    points = points - 16

elif option == "C":
    points = points + 25
else:
    print("Solo puedes responder: A, B y C")
    exit()

if points == 75:
    print("Felicidades, estoy orgulloso de ti, eres fan de Matos!")
elif points <= 37 or points <= 42:
    print("Acertaste 2 preguntas, genial!")

print("Tu puntaje es {}".format(points))
