# Descuento zoologico

# estos datos optan para descuento del 25%

# familia_numerosa = "artos integrantes"
# tercera_edad = "+65 a;os" "Tienen carnet de tercera edad"
# menor_edad = "tiene 10 o menos años"
# estudiante = "entre 25 y 35 años" "tiene carnet de estudiante"


edad = int(input("Cual es tu edad? :"))
tipo_carnet = input("Digame su tipo de carnet (E para Estudiante / T para Tercera Edad / F para Familia Numerosa / N "
                    "Nada) :")
# simpliflicando if (25 < edad < 35)
if (edad <= 35 and edad >= 25 and tipo_carnet == "E") or edad < 10 or (edad >= 65 and tipo_carnet == "T") or (tipo_carnet == "F"):
    print("Usted aplica para descuento")
else:
    print("Usted no aplicas para descuento, lo sentimos... ")

