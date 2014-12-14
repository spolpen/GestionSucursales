# coding=utf-8
__author__ = 'Polo'


class Sucursal():
    """Clase sucursal

    Esta clase define una sucursal, con listas de empleados, productos, proveedores e incidencias, y metodos para
    agregar y eliminar de dichas listas.
    
    """

    def __init__(self, nombre_sucursal, direccion, id_suc):
        """Constructor sucursal

        Metodo constructor de la clase sucursal, que inicializa sus atributos y ademas crea listas vacias para
        empleados, productos, proveedores e incidencias.


        :param nombre_sucursal:
        :param direccion:
        :param id_suc:
        :return:
        """

        self.nombre = nombre_sucursal
        self.direccion = direccion
        self.id = id_suc
        self.lista_emp = []
        self.lista_productos = []
        self.lista_proveedores = []
        self.lista_incidencias = []

    def aniadir_empleado(self, empleado):
        """Agregar empleado

        Agrega un empleado a la lista de empleados.

        :param empleado:
        :return:
        """
        self.lista_emp.append(empleado)

    def aniadir_producto(self, producto):
        """Agregar producto

        Agrega un producto a la lista de productos.

        :param producto:
        :return:
        """
        self.lista_productos.append(producto)

    def aniadir_incidencia(self, incidencia):
        """Agregar incidencia

        Agrega una incidencia a la lista de incidencias.

        :param incidencia:
        :return:
        """
        self.lista_incidencias.append(incidencia)

    def aniadir_proveedor(self, proveedor):
        """Agregar proveedor

        Agrega un proveedor a la lista de proveedores.

        :param proveedor:
        :return:
        """
        self.lista_proveedores.append(proveedor)

    def eliminar_empleado(self, empleado):
        """Eliminar empleado

        Elimina un empleado de la lista de empleados.

        :param empleado:
        :return:
        """
        ubicacion = self.lista_emp.index(empleado)
        del self.lista_emp[ubicacion]

    def eliminar_producto(self, producto):
        """Eliminar producto

        Elimina un producto de la lista de productos.

        :param producto:
        :return:
        """
        ubicacion = self.lista_productos.index(producto)
        del self.lista_productos[ubicacion]

    def eliminar_incidencia(self, incidencia):
        """Eliminar incidencia

        Elimina una incidencia de la lista de incidencias.

        :param incidencia:
        :return:
        """
        ubicacion = self.lista_incidencias.index(incidencia)
        del self.lista_incidencias[ubicacion]

    def eliminar_proveedor(self, proveedor):
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

    def get_id(self):
        """Get ID

        Metodo que devuelve la ID de la sucursal

        :return:ID sucursal
        """
        return self.id

    def get_listaproductos(self):
        """Get lista productos

        Metodo que devuelve la lista de productos de la sucursal

        :return:lista productos
        """
        return self.lista_productos

    def get_listaempleados(self):
        """Get lista empleados

        Metodo que devuelve la lista de empleados de la sucursal

        :return:lista empleados
        """
        return self.lista_emp

    def get_listaproveedores(self):
        """Get lista proveedores

        Metodo que devuelve la lista de proveedores de la sucursal

        :return:lista proveedores
        """
        return self.lista_proveedores

    def get_listaincidencias(self):
        """Get lista incidencias

        Metodo que devuelve la lista de incidencias de la sucursal

        :return:lista incidencias
        """
        return self.lista_incidencias

    def set_nombre(self, nombre):
        """Set nombre sucursal

        Cambia el nombre de la sucursal al parametro introducido.

        :param nombre:
        :return:
        """
        self.nombre = nombre

    def set_direccion(self, direccion):
        """Set direccion sucursal

        Cambia la direccion de la sucursal al parametro introducido.


        :param direccion:
        :return:
        """
        self.direccion = direccion

    def set_id(self, id_suc):
        """Set ID sucursal

        Cambia la ID de la sucursal al parametro introducido.

        :param id_suc:
        :return:
        """
        self.id = id_suc

    def get_salario_total(self):
        """Get salario total

        Calcula el salario total de los empleados de la sucursal.

        :param
        :return:salario total
        """
        num = 0
        for i in self.lista_emp:
            num += i.get_salario()
        return num

