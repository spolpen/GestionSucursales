__author__ = 'Raul'

class Sucursal():

    def __init__(self, nombre_sucursal, direccion, id):

        self.nombre = nombre_sucursal
        self.direccion = direccion
        self.id = id
        self.lista_emp = []
        self.lista_productos = []
        self.lista_incidencias = []

    def aniadirEmpleado(self,empleado):
        self.lista_emp.append(empleado)

    def aniadirProducto(self,producto):
        self.lista_productos.append(producto)

    def aniadirIncidencia(self,incidencia):
        self.lista_incidencias.append(incidencia)

    def eliminarEmpleado(self,empleado):
        ubicacion = self.lista_emp.index(empleado)
        del self.lista_emp[ubicacion]

    def eliminarProducto(self,producto):
        ubicacion = self.lista_productos.index(producto)
        del self.lista_productos[ubicacion]

    def eliminarIncidencia(self,incidencia):
        ubicacion = self.lista_incidencias.index(incidencia)
        del self.lista_incidencias[ubicacion]

    def eliminarIncidencia(self,incidencia):
        self.lista_incidencias.remove(incidencia)

    def getNombreSucursal(self):
        return self.nombre

    def getDireccionSucursal(self):
        return self.direccion

    def getIdSucursal(self):
        return self.id

    def get_salario_total(self):
        num=0
        for i in self.lista:
             num += i.get_salario()
        return num

    def salario_total_mensual(self):
        num = 0
        for i in self.lista:
            num += i.get_salario_mensual()
        return num