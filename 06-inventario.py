#Clase producto
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
interfaz = input("""
    MENU PRINCIPAL:
    1. Admin
    2. Usuario
    3. Salir
""")
