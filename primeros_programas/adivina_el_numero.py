#Adivina el numero!
#Teniendo en cuenta lo visto en esta clase, diseña un programa donde el usuario tenga que adivinar un numero de la
# secuencia del 1 al 10.
import random

print("Bienvenido al juego de adivinador")
print("tendras que adivinar el numero que tengamos en mente")
valor_adivinar = random.randint(0,10)

pregunta = input("Estas preparado para el reto? (s/n)")

if pregunta == "s":
    valor_usuario = int(input("Ingrese el numero que crea correcto: "))

    if valor_usuario == valor_adivinar:
        print("En hora buena, lo haz logrado")
    else:
        print("Lo sentimos, debe intentarlo de nuevo")

print(f"El valor era {valor_adivinar}")
print("El juego ha acabado")