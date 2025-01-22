#Esto sera un mini programa de test para saber a que casa Hogwarts perteneces

titulo2 = "Bienvenido al test Hogwarts, para saber a que faccion de Hogwarts perteneces:"
print("\n" + titulo2 + "-"*len(titulo2) + "\n")

facciones = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "ninguna"]

puntiacion2 = 0

pregunta_para_iniciar = input("Estas preparado para inicar?(s/n): \n")

if pregunta_para_iniciar == "s":
    print(f"Te mosntraremos las facciones: {facciones}\n"
          "elige la faccion con la cual sientas una afinidad\n")

    pregunta_para_faccion = input("Cual es la faccion la que sientes una afinidad?\n")

    if pregunta_para_faccion == "Gryffindor":
        print("Me alegro que hayas escogido Gryffindor\n"
              "Te hare unas preguntas a ver si eres digno de pertenecer aqui\n")

        pregunta_gryffindor = input("1. Un grupo de estudiantes está acosando a un compañero de primer año. ¿Qué "
                                    "haces\n?"
                                    "Respuestas:/n"
                                    "a.ntervengo de inmediato, aunque eso signifique enfrentarme al grupo. No puedo "
                                    "permitir que eso pase frente a mí.\n"
                                    "b.Primero analizo la situación y busco una forma inteligente de detenerlos sin "
                                    "arriesgarme demasiado.\n"
                                    "c.Intento hablar con los acosadores para calmar la situación de forma pacífica.\n"
                                    "d.Si no me afecta, me alejo. Pero si el estudiante puede serme útil, "
                                    "tal vez intervenga.\n")
        if pregunta_gryffindor == "a":
            print("Muy buena respuesta")
            puntiacion2 += 10
        elif pregunta_gryffindor == "b":
            print("No es mala respuesta, pero no me queda claro")
            puntiacion2 += 5
        elif pregunta_gryffindor == "c":
            print("Mmmm...")
            puntiacion2 += 2
        elif pregunta_gryffindor == "d":
            print("Por tu respuesta estoy muy seguro que no perteneces a esta faccion.")
            puntiacion2 += 0
        else:
            print("Porfa responde con una de las opciones dadas")
            exit()

        print("Es correcto. Tus respuestas son muy de un Gryffindor, eres digno")
    elif pregunta_para_faccion == "Hufflepuff":
        print("")
    elif pregunta_para_faccion == "Ravenclaw":
        print("")
    elif pregunta_para_faccion == "Slytherin":
        print("")
    elif pregunta_para_faccion == "ninguna":
        print("")
    else:
        print("Las opciones fueron mostrada, intentelo de nuevo")
        exit()

else:
    print("Hasta luego")
    exit()