#Inventario de tienda 

#Clase producto
class producto:
    def __init__(self,id, nombre, precio, cantidad, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

class inventario:
    def __init__(self):
        self.productos = {}