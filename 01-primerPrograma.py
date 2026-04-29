#Version inicial del curso
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))

print(f"El numero maximo es: ", {max(num1,num2,num3)})
print(f"El numero minimo es: ", {min(num1,num2,num3)})

# Version mas Pro
# def pedir_valor(cantidad):
#     numeros = []

#     for i in range(cantidad):
#         numero = int(input(f"Ingrese los numero {i+1}: "))
#         numeros.append(numero)
#     return numeros

# valor = pedir_valor(5)
# print(max(valor))
# print(min(valor))

