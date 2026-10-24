#Clase producto
import sys

class Producto:
    def __init__(self,id, nombre, precio, cantidad, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
    
    #Funciones del producto

#Clase Inventario
class Inventario:
    def __init__(self):
        self.dict_inventario = {}

    #Funciones para inventario

#Transformacion de las clases a objetos 
producto = Producto()
inventario = Inventario()

print("--- Bienvenido a la tiendo basai fantasia --- \n")
print("Elija una de las opciones: \n")

while True:
    interfaz = input("""
        MENU PRINCIPAL:
        1. Admin
        2. Usuario
        3. Salir
    """)
    if interfaz == "1":
        admin_eleccion = input("""
        OPCIONES DE INVENTARIO:
            1.Agregar Producto
            2.Buscar Producto
            3.Mostrar Producto
            4.Calcular Inventario
            5.Salir del Programa
        """)
        if admin_eleccion == "1":
            inventario.agregar_producto()

        if admin_eleccion == "2":
            inventario.buscar_producto()

        if admin_eleccion == "3":
            inventario.mostrar_producto()

        if admin_eleccion == "4":
            inventario.calcular_valor_inventario()

        if admin_eleccion == "5":
            print("Saliendo del programa...")
            sys.exit()
            break

    if interfaz == "2":
        usuario_eleccion = input("""
        OPCIONES DE INVENTARIO:
            1.Buscar Producto
            2.Comprar Producto
            3.Ver producto disponibles
            4.Salir del Programa
        """)
        if usuario_eleccion == "1":
            pass
        if usuario_eleccion == "2":
            pass
        if usuario_eleccion == "3":
            pass
        if usuario_eleccion == "4":
            print("Saliendo del programa...")
            sys.exit()
            break

    if interfaz == "3":
        print("Saliendo del programa...")
        sys.exit()
        break