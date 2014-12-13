__author__ = 'Polo'
from Persona import *

class Proveedor(Persona):
    """Clase proveedor

    Hereda de persona, pero no tiene atributos propios, de esta forma se distingue de empleado, que si tiene otros atributos.

    """
    def __init__(self, ID, DNI, nombre, telefono, direccion):
        """Constructor proveedor

        Metodo constructor de la clase proveedor, que hace uso del constructor de "Persona" para inicializar sus atributos.

        :param ID:
        :param DNI:
        :param nombre:
        :param telefono:
        :param direccion:
        :return:
        """
        Persona.__init__(self,ID, DNI, nombre, telefono, direccion)
