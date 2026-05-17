print("Bienvenido a la casa de cambio")

moneda = input("Opciones de cambios disponibles \n" \
                "1. De libras a Euros\n" \
                "2. De euros a libras\n" \
                "3. De euros a dolar\n"
                "Ingrese la opcion: ")

#Funciones de calculo
def librasEuros(libras):
    euros = libras * 1.15
    return euros

def euroLibras(euros):
    formLibras = 1/1.15
    libras = euros * formLibras
    return libras

def euroDolar(euro):
    dolar = euro * 1.16
    return dolar

#Comprobacion dependiendo la respuesta
if moneda == "1":
    cantidad = float(input("Ingrese la cantidad de Libras: "))
    resultado = librasEuros(cantidad)
    print(f"Su cambio a Euros es de: {resultado}")

elif moneda == "2":
    cantidad = float(input("Ingrese la cantidad de Euros: "))
    resultado = euroLibras(cantidad)
    print(f"Su cambio a Libras es de: {resultado}")

elif moneda == "3":
    cantidad = float(input("Ingrese la cantidad de Euros: "))
    resultado = euroDolar(cantidad)
    print(f"Su cambio a Dolares es de: {resultado}")

else:
    print("Solo se puede ingresar los opciones disponible, intentelo de nuevo")