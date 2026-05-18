import random

num = random.randint(1,10)
usuario = int(input("Ingrese el numero que cree que es: "))

if usuario == num:
    print("Ha acertado")

if usuario > 10 or usuario < 1:
    print("Porfavor ingrese un numero segun el rango")

print(f"Perdio, el numero era: {num}")