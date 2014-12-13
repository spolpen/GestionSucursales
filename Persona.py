__author__ = 'Polo'

class Persona(object):
    def __init__(self, ID, DNI, nombre, telefono, direccion):
        """Constructor persona

        Metodo constructor de la clase persona, que inicializa sus atributos con los parametros introducidos.

        :param ID:
        :param DNI:
        :param nombre:
        :param telefono:
        :param direccion:
        :return:
        """
        self.ID=ID
        self.DNI=DNI
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion

    def get_ID(self):
        """Get ID persona

        Metodo que devuelve la ID de la persona.

        :return:ID persona
        """
        return self.ID

    def get_DNI(self):
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

    def set_ID(self,ID):
        """Set ID persona

        Metodo que cambia la ID de la persona al parametro introducido.

        :param ID:
        :return:
        """
        self.ID=ID

    def set_DNI(self,DNI):
        """Set DNI persona

        Metodo que cambia el DNI de la persona al parametro introducido.

        :param DNI:
        :return:
        """
        self.DNI=DNI

    def set_nombre(self,nombre):
        """Set nombre persona

        Metodo que cambia el nombre de la persona al parametro introducido.

        :param nombre:
        :return:
        """
        self.nombre=nombre

    def set_telefono(self,telefono):
        """Set telefono persona

        Metodo que cambia el telefono de la persona al parametro introducido.

        :param telefono:
        :return:
        """
        self.telefono=telefono

    def set_direccion(self,direccion):
        """Set direccion persona

        Metodo que cambia la direccion de la persona al parametro introducido.

        :param direccion:
        :return:
        """
        self.direccion=direccion