__author__ = 'Polo'
from Persona import *

class Empleado(Persona):
    def __init__(self, ID, DNI, nombre, telefono, direccion, salario, horario):
        """Constructor empleado

        Metodo constructor de la clase empleado, que inicializa sus atributos que hereda de persona mediante el constructor de persona, ademas de los suyos propios.

        :param ID:
        :param DNI:
        :param nombre:
        :param telefono:
        :param direccion:
        :param salario:
        :param horario:
        :return:
        """
        Persona.__init__(self,ID, DNI, nombre, telefono, direccion)
        self.salario=salario
        self.horario=horario

    def get_salario(self):
        """Get salario empleado

        Metodo que devuelve el salario de un empleado

        :return:
        """
        return self.salario

    def get_horario(self):
        """Get horario empleado

        Metodo que devuelve el horario de un empleado.

        :return:
        """
        return self.horario

    def set_salario(self,salario):
        """Set salario empleado

        Metodo que cambia el salario del empleado al parametro introducido.

        :param salario:
        :return:
        """
        self.salario=salario

    def set_horario(self,horario):
        """Set horario empleado

        Metodo que cambia el horario de un empleado al parametro introducido.

        :param horario:
        :return:
        """
        self.horario=horario