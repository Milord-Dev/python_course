#varibles
respuesta = None
numero = 0

while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("Cual de las opciones elige [A,B,C]")

    if respuesta == "A":
        print("hola")

    elif respuesta == "B":
        print("como")

    elif respuesta == "C":
        print("estas?")

    else:
        print("no tiene sentido")

while 0 <= numero <= 20:
    print(f"este numero ira creciendo {numero}")
    numero += 1