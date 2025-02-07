import random

#Varibles de vida de los pokemones
vida_pikachu = 100
vida_bulbasaur = 100
vida_actual_pikachu = vida_pikachu
vida_actual_bulbasaur = vida_bulbasaur

while vida_pikachu > 0 and vida_bulbasaur > 0:
    #Turno de pikachu
    #variables de poder de pikachu
    bola_voltio = 10
    onda_truerno = 11
    num_ramd = random.randint(1,2)
    #calculo de porcentaje de vida de los pokemones
    porcentaje_vida_bulbasaur = int((vida_actual_bulbasaur * 10) / vida_bulbasaur)
    porcentaje_vida_pikachu = int((vida_actual_pikachu * 10) / vida_pikachu)

    #Ataques de pikachu
    print("Turno de Pikachu\n")
    if num_ramd == 1:
        vida_actual_bulbasaur -= bola_voltio
        print("Pikachi lanza Bola Voltio\n")
    else:
        vida_actual_bulbasaur -= onda_truerno
        print("Pikachi lanza Onda Trueno\n")

    print(f"La vida de pikachu bajo a: {"#" * porcentaje_vida_pikachu} {vida_actual_pikachu}%\n"
          f"La vida de bulbasaur bajo a: {"#" * porcentaje_vida_bulbasaur} {vida_actual_bulbasaur}%\n")

    input("Presione Enter para continuar...")

    #Turno de bulbasaur
    #varibles de poder de bulbasaur
    placaje = 10
    pistola_de_agua = 12
    burbuja = 9
    seleccion_ataque = None
    porcentaje_vida_bulbasaur = int((vida_actual_bulbasaur * 10)/vida_bulbasaur)
    porcentaje_vida_pikachu = int((vida_actual_pikachu * 10)/vida_pikachu)

    #Ataques de Bulbasaur
    while seleccion_ataque != "A" and seleccion_ataque != "B" and seleccion_ataque != "C":
        print("Turno de bulbasaur\n")
        seleccion_ataque = input("[A]PLACAJE: 10 DE DAÑO\n"
                                 "[B]PISTOLA DE AGUA: 12 DE DAÑO\n"
                                 "[C]BURBUJA: 9 DE DAÑO\n")

        if seleccion_ataque == "A":
            vida_actual_pikachu -= placaje
            print("Bulbasaur lanza Placaje\n")

        elif seleccion_ataque == "B":
            vida_actual_pikachu -= pistola_de_agua
            print("Bulbasaur lanza Pistola de Agua\n")

        elif seleccion_ataque == "C":
            vida_actual_pikachu -= burbuja
            print("Bulbasaur lanza Burbuja\n")

        else:
            print("Seleccione bien")

        print(f"La vida de pikachu bajo a: {"#" * porcentaje_vida_pikachu} {vida_actual_pikachu}%\n"
              f"La vida de bulbasaur bajo a: {"#" * porcentaje_vida_bulbasaur} {vida_actual_bulbasaur}%\n")

        input("Presione Enter para continuar...")

#Comprobacion de si gano uno u el otro
if vida_actual_pikachu > vida_actual_bulbasaur:
    print("Pikachu a ganado el combante")
else:
    print("Bulbasaur a ganado el combate")
