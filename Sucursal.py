__author__ = 'Polo'


class Sucursal():

    def __init__(self, nombre_sucursal, direccion, id):
        """Constructor sucursal

        Metodo constructor de la clase sucursal, que inicializa sus atributos y ademas crea listas vacias para empleados, productos, proveedores e incidencias.


        :param nombre_sucursal:
        :param direccion:
        :param id:
        :return:
        """

        self.nombre = nombre_sucursal
        self.direccion = direccion
        self.id = id
        self.lista_emp = []
        self.lista_productos = []
        self.lista_proveedores = []
        self.lista_incidencias = []


    def aniadirEmpleado(self,empleado):
        """Agregar empleado

        Agrega un empleado a la lista de empleados.

        :param empleado:
        :return:
        """
        self.lista_emp.append(empleado)

    def aniadirProducto(self,producto):
        """Agregar producto

        Agrega un producto a la lista de productos.

        :param producto:
        :return:
        """
        self.lista_productos.append(producto)

    def aniadirIncidencia(self,incidencia):
        """Agregar incidencia

        Agrega una incidencia a la lista de incidencias.

        :param incidencia:
        :return:
        """
        self.lista_incidencias.append(incidencia)

    def aniadirProveedor(self,proveedor):
        """Agregar proveedor

        Agrega un proveedor a la lista de proveedores.

        :param proveedor:
        :return:
        """
        self.lista_proveedores.append(proveedor)

    def eliminarEmpleado(self,empleado):
        """Eliminar empleado

        Elimina un empleado de la lista de empleados.

        :param empleado:
        :return:
        """
        ubicacion = self.lista_emp.index(empleado)
        del self.lista_emp[ubicacion]

    def eliminarProducto(self,producto):
        """Eliminar producto

        Elimina un producto de la lista de productos.

        :param producto:
        :return:
        """
        ubicacion = self.lista_productos.index(producto)
        del self.lista_productos[ubicacion]

    def eliminarIncidencia(self,incidencia):
        """Eliminar incidencia

        Elimina una incidencia de la lista de incidencias.

        :param incidencia:
        :return:
        """
        ubicacion = self.lista_incidencias.index(incidencia)
        del self.lista_incidencias[ubicacion]

    def eliminarProveedor(self,proveedor):
        """Eliminar proveedor

        Elimina un proveedor de la lista de proveedores.

        :param proveedor:
        :return:
        """
        ubicacion = self.lista_proveedores.index(proveedor)
        del self.lista_proveedores[ubicacion]

    def get_nombre(self):
        """Get nombre

        Metodo que devuelve el nombre de la sucursal

        :return:nombre sucursal
        """
        return self.nombre

    def get_direccion(self):
        """Get direccion

        Metodo que devuelve la direccion de la sucursal

        :return:direccion sucursal
        """
        return self.direccion

    def get_ID(self):
        """Get ID

        Metodo que devuelve la ID de la sucursal

        :return:ID sucursal
        """
        return self.id

    def get_listaProductos(self):
        """Get lista productos

        Metodo que devuelve la lista de productos de la sucursal

        :return:lista productos
        """
        return self.lista_productos

    def get_listaEmpleados(self):
        """Get lista empleados

        Metodo que devuelve la lista de empleados de la sucursal

        :return:lista empleados
        """
        return self.lista_emp

    def get_listaProveedores(self):
        """Get lista proveedores

        Metodo que devuelve la lista de proveedores de la sucursal

        :return:lista proveedores
        """
        return self.lista_proveedores

    def get_listaIncidencias(self):
        """Get lista incidencias

        Metodo que devuelve la lista de incidencias de la sucursal

        :return:lista incidencias
        """
        return self.lista_incidencias

    def set_nombre (self,nombre) :
        """Set nombre sucursal

        Cambia el nombre de la sucursal al parametro introducido.

        :param nombre:
        :return:
        """
        self.nombre=nombre

    def set_direccion (self,direccion):
        """Set direccion sucursal

        Cambia la direccion de la sucursal al parametro introducido.


        :
        :return:
        """
        self.direccion=direccion

    def set_ID(self,id):
        """Set ID sucursal

        Cambia la ID de la sucursal al parametro introducido.

        :param ID:
        :return:
        """
        self.id=id

    def get_salario_total(self):
        """Get salario total

        Calcula el salario total de los empleados de la sucursal.

        :param
        :return:salario total
        """
        num=0
        for i in self.lista_emp:
             num += i.get_salario()
        return num

