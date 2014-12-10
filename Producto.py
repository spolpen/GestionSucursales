__author__ = 'Polo'

class Producto:
    def __init__(self,ID, nombre, precio):
        self.ID=ID
        self.nombre=nombre
        self.precio=precio

    def get_ID(self):
        return self.ID

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def set_ID(self,ID):
        self.ID=ID

    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_precio(self,precio):
        self.precio=precio