#Crear un programa en el cual el usuario pueda introducir 3 numeros distintos y este pueda responder con el numero
# mas grande y el mas pequeño

numUsuario1 = int(input("Ingrese el valor de un numero: "))
numUsuario2 = int(input("Ingrese el valor de un numero: "))
numUsuario3 = int(input("Ingrese el valor de un numero: "))

numTotal = [numUsuario1,numUsuario2,numUsuario3]

print(f"El numero mayor es el: {max(numTotal)} y el numero menor es el: {min(numTotal)}")