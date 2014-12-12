__author__ = 'Polo'
from Persona import *

class Empleado(Persona):
    def __init__(self, ID, DNI, nombre, telefono, direccion, salario, horario):
        #super.__init__()
        Persona.__init__(self,ID, DNI, nombre, telefono, direccion)
        self.salario=salario
        self.horario=horario

    def get_salario(self):
        return self.salario

    def get_horario(self):
        return self.horario

    def set_salario(self,salario):
        self.salario=salario

    def set_horario(self,horario):
        self.horario=horario