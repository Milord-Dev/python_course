print("Bienvenido al Zoologico")
print("Comprobaremos su edad para ver si aplica al descuento")

pregunta_edad = int(input("Ingrese su edad: "))
tipo_carnet = input("Diga su tipo de carnet (E para estudiante) / P para pensionista / F para familia numerosa / N "
                    "para nada  ")

if ((25 <=pregunta_edad <= 35 and tipo_carnet == "E") or pregunta_edad < 10 or pregunta_edad > 65 and
        tipo_carnet == "P" or tipo_carnet == "F"):
    print("Usted recibe descuento")
else:
    print("No puede optar por un descuento")
