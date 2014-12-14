# coding=utf-8
__author__ = 'Polo'


class Persona(object):
    """Clase persona

    De esta clase heredan sus atributos las clases "Empleado" y "Proveedor"

    """

    def __init__(self, ide, dni, nombre, telefono, direccion):
        """Constructor persona

        Metodo constructor de la clase persona, que inicializa sus atributos con los parametros introducidos.

        :param ide:
        :param dni:
        :param nombre:
        :param telefono:
        :param direccion:
        :return:
        """
        self.ID = ide
        self.DNI = dni
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def get_id(self):
        """Get ID persona

        Metodo que devuelve la ID de la persona.

        :return:ID persona
        """
        return self.ID

    def get_dni(self):
        """Get ID persona

        Metodo que devuelve la ID de la persona.

        :return:ID persona
        """
        return self.DNI

    def get_nombre(self):
        """Get nombre persona

        Metodo que devuelve el nombre de la persona.

        :return:nombre persona
        """
        return self.nombre

    def get_telefono(self):
        """Get telefono persona

        Metodo que devuelve el telefono de la persona.

        :return:telefono persona
        """
        return self.telefono

    def get_direccion(self):
        """Get direccion persona

        Metodo que devuelve la direccion de la persona.

        :return:direccion persona
        """
        return self.direccion

    def set_id(self, ide):
        """Set ID persona

        Metodo que cambia la ID de la persona al parametro introducido.

        :param ide:
        :return:
        """
        self.ID = ide

    def set_dni(self, dni):
        """Set DNI persona

        Metodo que cambia el DNI de la persona al parametro introducido.

        :param dni:
        :return:
        """
        self.DNI = dni

    def set_nombre(self, nombre):
        """Set nombre persona

        Metodo que cambia el nombre de la persona al parametro introducido.

        :param nombre:
        :return:
        """
        self.nombre = nombre

    def set_telefono(self, telefono):
        """Set telefono persona

        Metodo que cambia el telefono de la persona al parametro introducido.

        :param telefono:
        :return:
        """
        self.telefono = telefono

    def set_direccion(self, direccion):
        """Set direccion persona

        Metodo que cambia la direccion de la persona al parametro introducido.

        :param direccion:
        :return:
        """
        self.direccion = direccion