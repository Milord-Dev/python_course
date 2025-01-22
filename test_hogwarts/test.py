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

        #Preguntas para gryffindor
        pregunta_gryffindor = input("1. Un grupo de estudiantes está acosando a un compañero de primer año. ¿Qué "
                                    "haces\n?"
                                    "Respuestas:/n"
                                    "a.Intervengo de inmediato, aunque eso signifique enfrentarme al grupo. No puedo "
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

        if puntiacion2 >= 5:
            print("Es correcto. Tus respuestas son muy de un Gryffindor, eres digno")
        else:
            print("Quizas deberias ir a otra faccion")

        #Preguntas Hufflepuff
    elif pregunta_para_faccion == "Hufflepuff":
        pregunta_hufflepuff = input("Un compañero olvidó su libro y no puede participar en clase. ¿Qué haces?\n"
                                    "Respuestas: \n"
                                    "a.Le presto mi libro o comparto el mío para que no se quede atrás.\n"
                                    "b.Le digo que debería haber estado más preparado, pero intento ayudarlo "
                                    "verbalmente.\n"
                                    "c.Le sugiero que pida uno prestado a otro estudiante o al profesor.\n"
                                    "d.No hago nada, su falta de preparación no es mi problema.\n")

        if pregunta_hufflepuff == "a":
            print("Muy buena respuesta")
            puntiacion2 += 10
        elif pregunta_hufflepuff == "b":
            print("No es mala respuesta, pero no me queda claro")
            puntiacion2 += 5
        elif pregunta_hufflepuff == "c":
            print("Mmmm...")
            puntiacion2 += 2
        elif pregunta_hufflepuff == "d":
            print("Por tu respuesta estoy muy seguro que no perteneces a esta faccion.")
            puntiacion2 += 0
        else:
            print("Porfa responde con una de las opciones dadas")
            exit()

        if puntiacion2 >= 5:
            print("Es correcto. Tus respuestas son muy de un Hufflepuff, eres digno")
        else:
            print("Quizas deberias ir a otra faccion")

        #Preguntas Ravenclaw
    elif pregunta_para_faccion == "Ravenclaw":
        pregunta_ravenclaw = input("Tu profesor menciona un tema avanzado que no estaba en los libros de estudio. "
                                   "¿Qué haces?\n"
                                   "a.Investigo más sobre el tema después de la clase. Quiero entenderlo a fondo "
                                   "aunque no sea obligatorio. \n"
                                   "b.Levanto la mano y pregunto en ese mismo momento, aunque no esté preparado.\n"
                                   "c.Le pido ayuda a un compañero que haya entendido mejor.\n"
                                   "d.Si el tema no afecta mi calificación, no pierdo tiempo en ello.\n")

        if pregunta_ravenclaw == "a":
            print("Muy buena respuesta")
            puntiacion2 += 10
        elif pregunta_ravenclaw == "b":
            print("No es mala respuesta, pero no me queda claro")
            puntiacion2 += 5
        elif pregunta_ravenclaw == "c":
            print("Mmmm...")
            puntiacion2 += 2
        elif pregunta_ravenclaw == "d":
            print("Por tu respuesta estoy muy seguro que no perteneces a esta faccion.")
            puntiacion2 += 0
        else:
            print("Porfa responde con una de las opciones dadas")
            exit()

        if puntiacion2 >= 5:
            print("Es correcto. Tus respuestas son muy Ravenclaw, eres digno")
        else:
            print("Quizas deberias ir a otra faccion")

        #Pregunta Slytherin
    elif pregunta_para_faccion == "Slytherin":
        pregunta_slytherin = input("Hay una competencia importante y sabes que un rival fuerte tiene una debilidad "
                                   "que podrías explotar. ¿Qué haces?\n"
                                  "a.Uso esa información para asegurar mi ventaja. Ganar es lo más importante.\n"
                                  "b.No exploto la debilidad. Prefiero ganar de manera justa, aunque sea más "
                                  "difícil.\n"
                                  "c.Estudio formas de superarlo sin necesidad de explotar su debilidad.\n"
                                  "d.Le advierto sobre su debilidad. No me sentiría bien ganando de esa manera.\n")

        if pregunta_slytherin== "a":
            print("Muy buena respuesta")
            puntiacion2 += 10
        elif pregunta_slytherin == "b":
            print("Mmmm...")
            puntiacion2 += 5
        elif pregunta_slytherin == "c":
            print("No...")
            puntiacion2 += 2
        elif pregunta_slytherin == "d":
            print("Jamas serias un Slytherin.")
            puntiacion2 += 0
        else:
            print("Porfa responde con una de las opciones dadas")
            exit()

        #Aqui la deje en 10 porque senti que slytherin no tiene afinidad con otras respuesta de las otras facciones o
        # casas
        if puntiacion2 >= 10:
            print("Es correcto. Tus respuestas son muy Slytherin, eres digno")
        else:
            print("Quizas deberias ir a otra faccion")


    elif pregunta_para_faccion == "ninguna":
        print("Que haces en Hogwarts?")
    else:
        print("Las opciones fueron mostrada, intentelo de nuevo")
        exit()

else:
    print("Hasta luego")
    exit()