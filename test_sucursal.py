# coding=utf-8
from unittest import TestCase
from Sucursal import *
from Empleado import *
from Incidencia import *
from Producto import *
from Proveedor import *
from mockito import *

__author__ = 'Polo'


class TestSucursal(TestCase):
    """Clase TestSucursal

    Esta clase contiene los tests unitarios para algunos metodos de la clase sucursal.

    """
    def test_get_salario_total(self):
        """Test get salario total

        Este test comprueba el correcto funcionamiento del metodo Get_salario_total de la clase sucursal.

        :return:
        """
        # Creamos mocks de Empleado
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(emp1).get_salario().thenReturn(1500)
        when(emp2).get_salario().thenReturn(1500)

        # Incluimos empleados
        suc.aniadir_empleado(emp1)
        suc.aniadir_empleado(emp2)
        # Hacemos el test
        self.assertEqual(suc.get_salario_total(), 3000)

    def test_aniadir_empleado(self):
        """Test aniadir empleado

        Este test comprueba que los empleados se agregan correctamente a la lista de empleados de la sucursal.

        :return:
        """
        # Creamos mocks de Empleado
        emp1 = mock(Empleado)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(emp1).get_ID().thenReturn(1)

        # Incluimos empleados
        suc.aniadir_empleado(emp1)
        lista = suc.get_listaempleados()
        # Hacemos el test
        self.assertEqual(lista[0].get_ID(), 1)

    def test_aniadir_producto(self):
        """Test aniadir producto

        Este test comprueba que los productos se agregan correctamente a la lista de productos de la sucursal.

        :return:
        """
        # Creamos mocks de Producto
        prod1 = mock(Producto)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(prod1).get_ID().thenReturn(1)

        # Incluimos producto
        suc.aniadir_producto(prod1)
        lista = suc.get_listaproductos()
        # Hacemos el test
        self.assertEqual(lista[0].get_ID(), 1)

    def test_aniadir_incidencia(self):
        """Test aniadir incidencia

        Este test comprueba que las incidencias se agregan correctamente a la lista de incidencias de la sucursal.

        :return:
        """
        # Creamos mocks de Incidencia
        inc1 = mock(Incidencia)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(inc1).get_id().thenReturn(1)

        # Incluimos incidencia
        suc.aniadir_incidencia(inc1)
        lista = suc.get_listaincidencias()
        # Hacemos el test
        self.assertEqual(lista[0].get_id(), 1)

    def test_aniadir_proveedor(self):
        """Test aniadir proveedor

        Este test comprueba que los proveedores se agregan correctamente a la lista de proveedores de la sucursal.

        :return:
        """
        # Creamos mocks de Proveedor
        pro1 = mock(Proveedor)

        # Creamos proveedor
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(pro1).get_ID().thenReturn(1)

        # Incluimos proveedor
        suc.aniadir_proveedor(pro1)
        lista = suc.get_listaproveedores()
        # Hacemos el test
        self.assertEqual(lista[0].get_ID(), 1)

    def test_eliminar_empleado(self):
        """Test eliminar empleado

        Este test comprueba que los empleados se eliminan correctamente de la lista de empleados de la sucursal.

        :return:
        """
        # Creamos mocks de Empleado
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Incluimos empleados
        suc.aniadir_empleado(emp1)
        suc.aniadir_empleado(emp2)
        # Eliminamos un empleado
        suc.eliminar_empleado(emp1)
        lista = suc.get_listaempleados()
        # Hacemos el test
        self.assertEqual(len(lista), 1)

    def test_eliminar_producto(self):
        """Test eliminar producto

        Este test comprueba que los productos se eliminan correctamente de la lista de productos de la sucursal.

        :return:
        """
        # Creamos mocks de Producto
        pro1 = mock(Producto)
        pro2 = mock(Producto)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Incluimos productos
        suc.aniadir_producto(pro1)
        suc.aniadir_producto(pro2)
        # Eliminamos un producto
        suc.eliminar_producto(pro1)
        lista = suc.get_listaproductos()
        # Hacemos el test
        self.assertEqual(len(lista), 1)

    def test_eliminar_incidencia(self):
        """Test eliminar incidencia

        Este test comprueba que las incidencias se eliminan correctamente de la lista de incidencias de la sucursal.

        :return:
        """
        # Creamos mocks de Incidencia
        inc1 = mock(Incidencia)
        inc2 = mock(Incidencia)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Incluimos incidencias
        suc.aniadir_incidencia(inc1)
        suc.aniadir_incidencia(inc2)
        # Eliminamos una incidencia
        suc.eliminar_incidencia(inc1)
        lista = suc.get_listaincidencias()
        # Hacemos el test
        self.assertEqual(len(lista), 1)

    def test_eliminar_proveedor(self):
        """Test eliminar proveedor

        Este test comprueba que los proveedores se eliminan correctamente de la lista de proveedores de la sucursal.

        :return:
        """
         # Creamos mocks de Proveedor
        pro1 = mock(Proveedor)
        pro2 = mock(Proveedor)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Incluimos proveedores
        suc.aniadir_proveedor(pro1)
        suc.aniadir_proveedor(pro2)
        # Eliminamos un proveedor
        suc.eliminar_proveedor(pro1)
        lista = suc.get_listaproveedores()
        # Hacemos el test
        self.assertEqual(len(lista), 1)