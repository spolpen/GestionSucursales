__author__ = 'Polo'
from Persona import *

class Proveedor(Persona):
    def __init__(self, ID, DNI, nombre, telefono, direccion):
        Persona.__init__(self,ID, DNI, nombre, telefono, direccion)
