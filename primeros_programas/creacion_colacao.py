print("Bienvenido a como crear tu propio colacao")
print("Te hare preguntas y mediantes vayas respondiendo te dare una instruccion u otra")

pregunta1 = input("Estas preparado?(s/n): ")

if pregunta1 == "s":
    print("Iniciaremos con la primera instruccion")
    print("Revisa si en tu nevera se encuentra una caja de leche y si tienes colacao")

pregunta2 = input("Hay leche en tu nevera (s/n): ")
pregunta3 = input("Hay colacao en alguna parte? (s/n): ")

if pregunta2 != "s" or pregunta3 != "s":
        print("Ve al super")
        if pregunta2 != "s":
            print("Compra una caja de leche")
        if pregunta3 != "s":
            print("Compramos un paquete de colacao")

print("ve y busca un vaso para echar la leche junto al colacao (no creo que no vayas a tener un vaso ._.)")
print("mezcla la leche con el colacao")

