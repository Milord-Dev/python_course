#FINAL BOSS
# Realiza tu propia mazmorra con tus variables, personajes, tiempo ilimitado, etcétera. Solo debes cumplir con estos
# dos requisitos Tiene que contener un desafío aritmético.
# Tiene que contener uno o varios objetos que se deben recoger y comprobar si el usuario los tiene o no.¡Mucha suerte!

import random
from operator import truediv

mensaje_de_perdedor = "Haz perdido..."
mensaje_de_salida = "Regresa cuando te sientas preparado"
titulo = "BIENVENIDO A THE TIME IS OVER"
print("\n" + titulo + "\n" + "="*len(titulo) + "\n")

personajes = ["Akira","Katsumi"]
print(f"Los personajes que puedes elegir son: {personajes} \n")

pregunta_de_seleccion = input("Cual personaje prefiere: \n")

if pregunta_de_seleccion == "Akira":
    print("Has elegido a AKIRA, la guerrera dragon! \n")
    pregunta_de_inicio = input("Estas preparado para entrar a la mazmorra?(S/N): \n")

    if pregunta_de_inicio == "S":
        print("LAS PROFUNDIDADES DE UMBRA")
        print("---------------------------\n")
        print("Oculta en un bosque sombrío, esta mazmorra fue un santuario para el culto\n"
              "de Umbra, diosa de las sombras. Sellada por magia tras oscuros rituales,su\n"
              "entrada ahora emite susurros que atraen a los curiosos. En su interior,\n"
              "sombras vivientes acechan y protegen el legendario Espejo de Umbra, un\n"
              "artefacto que concede deseos a cambio de la cordura. Pocos regresan; la\n"
              "oscuridad siempre cobra su precio.\n")
        print("Objetivo de la mazmorra: Obtener el ESPEJO DE UMBRA\n")

        print("Te paras frente a la entrada de la mazmorra, el aire denso y cargado de misterio.\n"
              "Dos caminos se abren ante ti: \n"
              "[OPCIÓN A]: A la izquierda, un túnel sumido en una oscuridad casi total.\n"
              "[OPCIÓN B]: A la derecha, un sendero rodeado de árboles retorcidos y envuelto en niebla.\n")

        #ELECCION DE CAMINO
        respuesta = input("Cual de los 2 caminos escoges?: \n")
        if respuesta == "A":
            print("Has decidido adentrarte en el tunel de la oscuridad.\n"
                  "Bienvenido, viajero valiente, es lo que dice un espectro al fondo de la cueva con\n"
                  "una voz grave y resonante. Resuelve mi acertijo o quedarás atrapado aquí para siempre.\n")

            # SELECCION DE RESPUESTAS
            pregunta_akira = input("ACERTIJO:\n"
                                   "En la oscuridad siempre estoy, pero cuando llega la luz, desaparezco\n"
                                   "sin dejar rastro. ¿Quién soy?\n"
                                   "[OPCIÓN A]: La sombra\n"
                                   "[OPCIÓN B]: El miedo\n"
                                   "[OPCIÓN C]: La noche\n")

            if pregunta_akira == "A":
                print("El espectro asiente y dice: Has hablado con verdad. La luz guiará tu camino.El túnel\n"
                      "se ilumina y puedes continuar.\n")

                #SEGUIRA AL SIGUIENTE CAMINO
                espejo_de_umbra = False

                print("El túnel se ilumina con una tenue luz azulada que parpadea a medida que avanzas.\n"
                      "La sombra del espectro se desvanece detrás de ti, y pronto te encuentras en una gran sala de\n"
                      "piedra cubierta de inscripciones antiguas. En el centro, una figura encorvada con un báculo \n "
                      "de hueso e observa con ojos vacíos.\n"
                      "Has demostrado sabiduría, pero aún no eres digno de seguir adelante.\n"
                      "Si deseas cruzar este umbral, debes superar una última prueba.\n")

                pregunta_akira = input("Si sumas dos veces mi número a sí mismo, obtienes 24. ¿Qué número soy?\n"
                      "[OPCION A]: 6\n"
                      "[OPCION B]: 8\n"
                      "[OPCION C]: 12\n")

                if pregunta_akira == "A":
                    espejo_de_umbra = True
                    print("La figura sonríe levemente. Has resuelto el enigma. La puerta se abrirá para ti.\n"
                          "Un portal de luz se forma al fondo de la sala, permitiéndote avanzar.\n"
                          "Al salir cae en tus manos el ESPEJO DE UMBRA")

                    #SIGUIENTE CAMINO:
                    print("Al cruzar el portal, te encuentras en una enorme sala oscura. En el centro, un ser\n"
                          "imponente con ojos rojos te observa desde un trono de sombras. Su voz retumba en el\n"
                          "aire:\n"
                          "Has llegado lejos, viajero. Responde con la verdad.\n"
                          "¿Tienes el Espejo de Umbra?")

                    if espejo_de_umbra == True:
                        print("Haz superado la Mazmorra viajero. Suerte en tu camino")
                        exit()
                    else:
                        print(mensaje_de_perdedor)
                        exit()
                else:
                    print("La criatura sacude la cabeza. No. No mereces avanzar.\n")
                    print(mensaje_de_perdedor)
                    exit()
            else:
                print("El espectro ríe con frialdad. El miedo no desaparece con la luz y tampoco se oculta en la\n"
                      "noche\n")
                print(mensaje_de_perdedor)
                exit()

        # SELECCION DE RESPUESTAS
        elif respuesta == "B":
            print("El suelo es pantanoso y cada paso parece más pesado. De repente, una silueta emerge entre la\n"
                  "bruma: una criatura alta con cuernos retorcidos y ojos dorados que brillan en la oscuridad.\n")

            num_ramdom = random.randint(1, 10)
            pregunta_akira = input("DESAFÍO ARITMÉTICO:\n"
                                   f"Tengo 10 milenios, si multiplicas mi edad por 3 y le sumas: {num_ramdom} cuanta\n"
                                   f"edad tendria?\n"
                                   "Espero tu respuesta...: \n")
            respuesta = pregunta_akira

            if pregunta_akira == respuesta:
                print("La criatura asiente y la niebla comienza a disiparse. Eres sabio, viajero. Continúa tu\n"
                      "camino. El pantano parece menos denso, y puedes avanzar sin peligro.\n")
                #SEGUIRA AL SIGUIENTE CAMINO
                print("A pesar de haber respondido correctamente, el monstruo solo deja escapar una risa grave y\n"
                      "burlona."
                      "Digno... ¿tú?Su voz retumba en la sala mientras la oscuridad se arremolina a su alrededor.\n"
                      "Todos los aventureros creen merecerlo. Pero yo… yo detesto a los intrusos.")
                print(mensaje_de_perdedor)
                exit()
            else:
                print(mensaje_de_perdedor)
                exit()
        else:
            print(mensaje_de_salida)
            exit()
    else:
        print(mensaje_de_salida)
        exit()

elif pregunta_de_seleccion == "Katsumi":
    print("Has ejelegido a KATSUMI, samurai de las tinieblas!")
    pregunta_de_inicio = input("Estas preparado para entrar a la mazmorra?(S/N): ")

    if pregunta_de_inicio == "S":
        print("LAS PROFUNDIDADES DE RAITZA")
        print("----------------------------\n")
        print("La entrada de la mazmorra se abre con un crujido aterrador. Un espeso velo de neblina oscura serpentea\n"
              "por el suelo, y el aire vibra con una energía inquietante, como si algo antiguo y olvidado te estuviera\n"
              "observando.Frente a ti, dos caminos emergen de las sombras. ¿Cuál eliges?\n"
              "[OPCIÓN A]: A la izquierda, una puerta de madera repleta de raices con espinas y una luz muy tenue.\n"
              "[OPCIÓN B]: A la derecha, una puerta de hierro templado, envuelta en una gruesa capa de hielo.\n")
        print("Objetivo de la mazmorra: Obtener la ESPADA DE RAITZA\n")

        respuesta = input("Cual de los 2 caminos escoges?: \n")

        if respuesta == "A":
            print("El suelo es pantanoso y cada paso parece más pesado. De repente, una silueta emerge entre la\n"
                  "bruma: una criatura alta con cuernos retorcidos y ojos dorados que brillan en la oscuridad.\n")

            num_ramdom = random.randint(1, 10)
            pregunta_akira = input("DESAFÍO ARITMÉTICO:\n"
                                   f"Tengo 5 milenios, si multiplicas mi edad por 5 y le sumas: {num_ramdom} cuanta\n"
                                   f"edad tendria?\n"
                                   "Espero tu respuesta...: \n")
            respuesta = pregunta_akira

            if pregunta_akira == respuesta:
                print("La criatura asiente y la niebla comienza a disiparse. Has elegido bien, viajero. Sigue tu\n"
                      "camino. El pantano parece menos denso, permitiéndote avanzar sin peligro.\n")
                print("Aunque tu respuesta fue correcta, el monstruo suelta una risa grave y burlona.\n"
                      "¿Digno... tú? Su voz resuena en la sala mientras la oscuridad se agita a su alrededor.\n"
                      "Todos los aventureros creen merecerlo. Pero yo… yo detesto a los intrusos.")
                print(mensaje_de_perdedor)
                exit()
            else:
                print(mensaje_de_perdedor)
                exit()

        if respuesta == "B":
            print("\nEl aire es gélido y tu aliento se convierte en nubes de vapor. La puerta de hierro se abre\n"
                  "lentamente con un rechinar metálico. Al otro lado, un pasillo helado conduce a una gran cámara.\n"
                  "En su centro, una estatua de hielo con forma de guerrero sostiene una espada incrustada en un pedestal.\n")
            print("Para reclamar la ESPADA DE RAITZA, debes probar tu mente, no tu espada.\n")

            pregunta_akira = input("ACERTIJO DE RAITZA:\n"
                                   "Cuanto más tomas de mí, más grande me vuelvo. ¿Qué soy?\n"
                                   "[OPCIÓN A]: La sombra\n"
                                   "[OPCIÓN B]: Un agujero\n"
                                   "[OPCIÓN C]: El tiempo\n")
            if pregunta_akira == "B":
                print("\nLa estatua de hielo comienza a agrietarse y la sala tiembla.\n"
                      "‘Has respondido con sabiduría, viajero. La Espada de Raitza es tuya.’\n")
                espada_de_raitza = True

                print("Al tomar la espada, la temperatura de la sala aumenta y la estatua se desmorona en polvo de "
                      "hielo. Un portal de energía oscura se abre al fondo de la cámara. Sin dudarlo, atraviesas el\n"
                      "umbral.\n"
                      "\nTe encuentras en una vasta sala de piedra, iluminada solo por antorchas espectrales.\n"
                      "En el centro, un trono de obsidiana sostiene una figura encapuchada con ojos rojos fulgurantes.\n"
                      "‘Has llegado lejos, viajero… pero dime… ¿Portas la Espada de Raitza?’\n")

                if espada_de_raitza == True:
                    print("\n‘Tu valentía y astucia te han llevado lejos. Has superado la Mazmorra de Raitza.’\n"
                          "Con un gesto de su mano, el trono se disuelve en sombras y una puerta dorada aparece ante ti.\n"
                          "‘El destino de este mundo está en tus manos. Sigue adelante, guerrero.’\n")
                    exit()
                else:
                    print("\nLa figura entorna los ojos. ‘Has llegado lejos, pero sin la Espada de Raitza,\n"
                          "no eres digno de continuar.’\n")
                    print(mensaje_de_perdedor)
                    exit()
            else:
                print("No has elegido un camino válido. La mazmorra se estremece y la oscuridad te envuelve.\n")
                print(mensaje_de_perdedor)
                exit()

    else:
        print(mensaje_de_salida)
        exit()

else:
    print("Solo podias escoger entre Akira y Katsumi")
    exit()