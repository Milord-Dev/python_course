#Escoge tu nuevo movil con las siguientes preguntas
titulo3 = "Bienvenido, te ayudaremos a seleccionar tu nuevo movil"

print("\n" + titulo3 + "\n" + "-"*len(titulo3) + "\n")

print("Seleccione uno de los siguientes modelos: \n")
pregunta_usuario = input("[android o ios]: ")

if pregunta_usuario == "android":
    pregunta_dinero = input("Tienes dinero?(s/n): ")

    if pregunta_dinero == "s":
        pregunta_camara = input("Te importa la camara?(s/n): ")
        if pregunta_camara == "s":
            print("Comprate un Google Pixel SuperCamara")
        elif pregunta_camara == "n":
            print("Puedes comprarte un Android calidad-precio")
        else:
            print("Solo puedes seleccionar s o n")
            exit()

    elif pregunta_dinero == "n":
        print("Ps... toco comprar el barato (android chino)")

    else:
        print("Solo puedes seleccionar s o n")
        exit()

elif pregunta_usuario == "ios":
    pregunta_dinero = input("Tienes dinero?(s/n): ")

    if pregunta_dinero == "s":
        print("Puedes comprarte un Iphone Ultra Pro Max")

    elif pregunta_dinero == "n":
        print("Toca comprar uno de segunda bro...")

    else:
        print("Solo puedes seleccionar s o n")

else:
    print("Solo podias selecionar entre android o ios")
    exit()
