# coding=utf-8
__author__ = 'Polo'
from Persona import *


class Empleado(Persona):
    """Clase empleado

    Esta clase hereda de persona y ademas tiene varios atributos propios como el salario y el horario.

    """

    def __init__(self, ide, dni, nombre, telefono, direccion, salario, horario):
        """Constructor empleado

        Metodo constructor de la clase empleado, que inicializa sus atributos que hereda de persona
         mediante el constructor de persona, ademas de los suyos propios.

        :param ide:
        :param dni:
        :param nombre:
        :param telefono:
        :param direccion:
        :param salario:
        :param horario:
        :return:
        """
        Persona.__init__(self, ide, dni, nombre, telefono, direccion)
        self.salario = salario
        self.horario = horario

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

    def set_salario(self, salario):
        """Set salario empleado

        Metodo que cambia el salario del empleado al parametro introducido.

        :param salario:
        :return:
        """
        self.salario = salario

    def set_horario(self, horario):
        """Set horario empleado

        Metodo que cambia el horario de un empleado al parametro introducido.

        :param horario:
        :return:
        """
        self.horario = horario