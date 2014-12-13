__author__ = 'Polo'


class Sucursal():

    def __init__(self, nombre_sucursal, direccion, id):

        self.nombre = nombre_sucursal
        self.direccion = direccion
        self.id = id
        self.lista_emp = []
        self.lista_productos = []
        self.lista_proveedores = []
        self.lista_incidencias = []


    def aniadirEmpleado(self,empleado):
        self.lista_emp.append(empleado)

    def aniadirProducto(self,producto):
        self.lista_productos.append(producto)

    def aniadirIncidencia(self,incidencia):
        self.lista_incidencias.append(incidencia)

    def aniadirProveedor(self,proveedor):
        self.lista_proveedores.append(proveedor)

    def eliminarEmpleado(self,empleado):
        ubicacion = self.lista_emp.index(empleado)
        del self.lista_emp[ubicacion]

    def eliminarProducto(self,producto):
        ubicacion = self.lista_productos.index(producto)
        del self.lista_productos[ubicacion]

    def eliminarIncidencia(self,incidencia):
        ubicacion = self.lista_incidencias.index(incidencia)
        del self.lista_incidencias[ubicacion]

    def eliminarProveedor(self,empleado):
        ubicacion = self.lista_proveedores.index(empleado)
        del self.lista_proveedores[ubicacion]

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_ID(self):
        return self.id

    def get_listaProductos(self):
        return self.lista_productos

    def get_listaEmpleados(self):
        return self.lista_emp

    def get_listaProveedores(self):
        return self.lista_proveedores

    def get_listaIncidencias(self):
        return self.lista_incidencias

    def set_nombre (self,nombre) :
        self.nombre=nombre

    def set_direccion (self,direccion):
        self.direccion=direccion

    def set_ID(self,id):
        self.id=id

    def get_salario_total(self):
        num=0
        for i in self.lista_emp:
             num += i.get_salario()
        return num

