titulo = "Bienvenido al Test del queso"
print("\n" + titulo + "\n" + "-"*len(titulo) + "\n")

puntiacion = 0

opcion = input("Pregunta 1: Que haces cuando ves una tabla de queso? \n"
               "A. Salgo corriendo\n"
               "B. Pruebo uno de los quesos o incluso varios\n"
               "C. No puedo evitar devorarla")

if opcion == "A":
    puntiacion += 0

elif opcion == "B":
    puntiacion += 5

elif opcion == "C":
    puntiacion += 10
else:
    print("Las opciones posibles son (a,b,c)")
    exit()

opcion = input("Pregunta 2: Como te gusta la hamburguesa? \n"
               "A. Sin queso\n"
               "B. Con queso\n"
               "C. Extra queso")

if opcion == "A":
    puntiacion += 0

elif opcion == "B":
    puntiacion += 5

elif opcion == "C":
    puntiacion += 10
else:
    print("Las opciones posibles son (a,b,c)")
    exit()

opcion = input("Pregunta 3: Eres intolerante a la lactosa? \n"
               "A. Si\n"
               "B. A veces\n"
               "C. No")

if opcion == "A":
    puntiacion += 0

elif opcion == "B":
    puntiacion += 5

elif opcion == "C":
    puntiacion += 10
else:
    print("Las opciones posibles son (a,b,c)")
    exit()

print(f"Su puntuacion fue: {puntiacion}")
if puntiacion >= 25:
    print("Eres fanatico del queso")
elif puntiacion >= 15:
    print("Eres quizas un fanatico del queso")
else:
    print("Solo no te gusta el queso")
