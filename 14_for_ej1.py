# ejemplo de nate

# output esperado
# espacios = 6
# puntos = 1
# comas = 1

texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?"

espacios_texto = " "
puntos_texto = "."
comas_texto= ","

espacios_encontrados = 0
puntos_encontrados = 0
comas_encontrados = 0

for letra in texto_usuario:
    if letra in espacios_texto:
        espacios_encontrados += 1
    elif letra in puntos_texto:
        puntos_encontrados += 1
    elif letra in comas_texto:
        comas_encontrados += 1

print("Espacios encontrados: {}".format(espacios_encontrados))
print("Puntos encontrados: {}".format(puntos_encontrados))
print("Comas encontrados: {}".format(comas_encontrados))