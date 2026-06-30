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
    def estado_producto():
        pass

    def reponer_stock():
        pass

    def calcular_precio_producto():
        pass

#Clase Inventario
class Inventario:
    def __init__(self):
        self.dict_inventario = {}

    #Funciones para inventario
    def agregar_producto():
        pass

    def buscar_producto():
        pass

    def mostrar_producto():
        pass

    def calcular_valor_inventario():
        pass

    def notificacion_producto():
        pass

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

    if interfaz == "2":
        usuario_eleccion = input("""
        OPCIONES DE INVENTARIO:
            1.Buscar Producto
            2.Comprar Producto
            3.Ver producto disponibles
            4.Salir del Programa
        """)

    if interfaz == "3":
        print("Saliendo del programa...")
        sys.exit()
        break