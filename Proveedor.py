__author__ = 'Polo'

class Proveedor:
    def __init__(self, ID, DNI, nombre, telefono, direccion):
        self.ID=ID
        self.DNI=DNI
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion

    def get_ID(self):
        return self.ID

    def get_DNI(self):
        return self.DNI

    def get_nombre(self):
        return self.nombre

    def get_telefono(self):
        return self.telefono

    def get_direccion(self):
        return self.direccion

    def set_ID(self,ID):
        self.ID=ID

    def set_DNI(self,DNI):
        self.DNI=DNI

    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_telefono(self,telefono):
        self.telefono=telefono

    def set_direccion(self,direccion):
        self.direccion=direccion