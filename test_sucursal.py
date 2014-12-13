from unittest import TestCase
from Sucursal import *
from Empleado import *
from Incidencia import *
from Producto import *
from Proveedor import *
from mockito import *

__author__ = 'Polo'


class TestSucursal(TestCase):
    def test_get_salario_total(self):
        # Creamos mocks de Empleado
        Emp1 = mock(Empleado)
        Emp2 = mock(Empleado)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(Emp1).get_salario().thenReturn(1500)
        when(Emp2).get_salario().thenReturn(1500)

        # Incluimos empleados
        suc.aniadirEmpleado(Emp1)
        suc.aniadirEmpleado(Emp2)
        # Hacemos el test
        self.assertEqual(suc.get_salario_total(), 3000)


class TestSucursal(TestCase):
    def test_aniadirEmpleado(self):
        # Creamos mocks de Empleado
        Emp1 = mock(Empleado)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(Emp1).get_ID().thenReturn(1)

        # Incluimos empleados
        suc.aniadirEmpleado(Emp1)
        lista = suc.get_listaEmpleados()
        # Hacemos el test
        self.assertEqual(lista[0].get_ID(), 1)


class TestSucursal(TestCase):
    def test_aniadirProducto(self):
        # Creamos mocks de Producto
        Prod1 = mock(Producto)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(Prod1).get_ID().thenReturn(1)

        # Incluimos producto
        suc.aniadirProducto(Prod1)
        lista = suc.get_listaProductos()
        # Hacemos el test
        self.assertEqual(lista[0].get_ID(), 1)


class TestSucursal(TestCase):
    def test_aniadirIncidencia(self):
        # Creamos mocks de Incidencia
        Inc1 = mock(Incidencia)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(Inc1).get_ID().thenReturn(1)

        # Incluimos incidencia
        suc.aniadirIncidencia(Inc1)
        lista = suc.get_listaIncidencias()
        # Hacemos el test
        self.assertEqual(lista[0].get_ID(), 1)


class TestSucursal(TestCase):
    def test_aniadirProveedor(self):
        # Creamos mocks de Proveedor
        Pro1 = mock(Proveedor)

        # Creamos proveedor
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Simulamos comportamiento
        when(Pro1).get_ID().thenReturn(1)

        # Incluimos proveedor
        suc.aniadirProveedor(Pro1)
        lista = suc.get_listaProveedores()
        # Hacemos el test
        self.assertEqual(lista[0].get_ID(), 1)


class TestSucursal(TestCase):
    def test_eliminarEmpleado(self):
        # Creamos mocks de Empleado
        Emp1 = mock(Empleado)
        Emp2 = mock(Empleado)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Incluimos empleados
        suc.aniadirEmpleado(Emp1)
        suc.aniadirEmpleado(Emp2)
        # Eliminamos un empleado
        suc.eliminarEmpleado(Emp1)
        lista = suc.get_listaEmpleados()
        # Hacemos el test
        self.assertEqual(len(lista), 1)


class TestSucursal(TestCase):
    def test_eliminarProducto(self):
        # Creamos mocks de Producto
        Pro1 = mock(Producto)
        Pro2 = mock(Producto)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Incluimos productos
        suc.aniadirProducto(Pro1)
        suc.aniadirProducto(Pro2)
        # Eliminamos un producto
        suc.eliminarProducto(Pro1)
        lista = suc.get_listaProductos()
        # Hacemos el test
        self.assertEqual(len(lista), 1)


class TestSucursal(TestCase):
    def test_eliminarIncidencia(self):
        # Creamos mocks de Incidencia
        Inc1 = mock(Incidencia)
        Inc2 = mock(Incidencia)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Incluimos incidencias
        suc.aniadirIncidencia(Inc1)
        suc.aniadirIncidencia(Inc2)
        # Eliminamos una incidencia
        suc.eliminarIncidencia(Inc1)
        lista = suc.get_listaIncidencias()
        # Hacemos el test
        self.assertEqual(len(lista), 1)


class TestSucursal(TestCase):
    def test_eliminarProveedor(self):
         # Creamos mocks de Proveedor
        Pro1 = mock(Proveedor)
        Pro2 = mock(Proveedor)

        # Creamos sucursal
        suc = Sucursal("Sevilla", "Pino Montano", "Sucursal1")

        # Incluimos proveedores
        suc.aniadirProveedor(Pro1)
        suc.aniadirProveedor(Pro2)
        # Eliminamos un proveedor
        suc.eliminarProveedor(Pro1)
        lista = suc.get_listaProveedores()
        # Hacemos el test
        self.assertEqual(len(lista), 1)