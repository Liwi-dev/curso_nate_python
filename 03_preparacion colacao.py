

print("me voy a la cocina")
print("abro la nevera")

hay_leche = input("Hay leche? (si/no) ")
hay_colacao = input("Hay colacao? (si/no)")
hay_nesquik = input("Hay nesquik? (si/no)")
hay_bebida_colacao = input("Hay bebida colacao? (si/no)")

if hay_leche != "si" or hay_colacao != "si":
    print("A comprar al supermercado!")
    if hay_leche != "si":
        print("Compro leche!")
    if hay_colacao != "si":
        print("Compro colacao!")

if hay_leche == "si" and hay_colacao == "si" or hay_leche == "si" and hay_nesquik == "si":
    print("ponemos la leche en el vaso")
    print("ponemos el colacao en el vaso")
    print("Mezclamos")

if hay_bebida_colacao == "si":
    print("Bebemos la bebida colacao y después a comprar al super")