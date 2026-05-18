print("Preparacion de colacao")

pregunta1 = input("Hay leche en la nevera? \n" \
                    "Responder s en caso de tenerlo \n" \
                    "Responde n en caso de no tenerlo \n" \
                    "Respuesta: ")

pregunta2 = input("Hay colacao en la nevera? \n" \
                    "Responder s en caso de tenerlo \n" \
                    "Responde n en caso de no tenerlo \n" \
                    "Respuesta: ")

if pregunta1 != "s" or pregunta2 != "s":
    print("Voy al super...")
    if pregunta1 != "s":
        print("Voy al super a comprar leche")
    if pregunta2 != "s":
        print("voy al super a comprar colacao")


print("1. Ponemos la leche en el vaso \n" \
        "2. Ponemos el colacao \n" \
        "3. Mezclamos el colacao con la leche.")