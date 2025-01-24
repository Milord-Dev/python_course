#Conversor de divisas
#Varibles
dolar_eur = 0.96
dolar_libra = 0.81
euro_dolar = 1.04
libra_eur = 1.19
libra_dolar = 1.24
euro_libra = 0.84

titulo2 = "Bienvenido al conversor de divisas"
print("\n" + titulo2 + "\n" + "-"*len(titulo2) + "\n")

print("Divisas disponibles: dolar, euro, libra")
pregunta_divisa_actual = input("Ingrese la divisa la divisa que tiene: ")

#Proceso de dolar
if pregunta_divisa_actual == "dolar":
    print("Recuerde que solo puede convertirla a euro o libra")
    pregunta_divisa_convertida = input("Ingrese a cual divisa la quiere converti: ")

    if pregunta_divisa_convertida == "euro":
        cantidad = float(input("Ingrese la cantidad que tiene: "))
        print(f"Su nuevo balance es de: {cantidad*dolar_eur}")

    elif pregunta_divisa_convertida == "libra":
        cantidad = float(input("Ingrese la cantidad que tiene: "))
        print(f"Su nuevo balance es de: {cantidad*dolar_libra}")

    else:
        print("fijese bien en la divisas seleccionadas")
        exit()


#Proceso de euro
elif pregunta_divisa_actual == "euro":
    print("Recuerde que solo puede convertirla a dolar o libra")
    pregunta_divisa_convertida = input("Ingrese a cual divisa la quiere converti: ")

    if pregunta_divisa_convertida == "dolar":
        cantidad = float(input("Ingrese la cantidad que tiene: "))
        print(f"Su nuevo balance es de: {cantidad*euro_dolar}")

    elif pregunta_divisa_convertida == "libra":
        cantidad = float(input("Ingrese la cantidad que tiene: "))
        print(f"Su nuevo balance es de: {cantidad * euro_libra}")

    else:
        print("fijese bien en la divisas seleccionadas")
        exit()


#Proceso de Libra
elif pregunta_divisa_actual == "libra":
    print("Recuerde que solo puede convertirla a dolar o euro")
    pregunta_divisa_convertida = input("Ingrese a cual divisa la quiere converti: ")

    if pregunta_divisa_convertida == "dolar":
        cantidad = float(input("Ingrese la cantidad que tiene: "))
        print(f"Su nuevo balance es de: {cantidad * libra_dolar}")

    elif pregunta_divisa_convertida == "euro":
        cantidad = float(input("Ingrese la cantidad que tiene: "))
        print(f"Su nuevo balance es de: {cantidad * libra_eur}")

    else:
        print("fijese bien en la divisas seleccionadas")
        exit()