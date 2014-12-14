# coding=utf-8
from unittest import TestCase
from Incidencia import *

__author__ = 'Polo'


class TestIncidencia(TestCase):
    """Clase TestSucursal

    Esta clase contiene los tests unitarios de la clase incidencia..

    """

    def test_resolver(self):
        """Test resolver

        Este test comprueba el correcto funcionamiento del metodo resolver de la clase incidencia.

        :return:
        """
        inc = Incidencia(1, "Asunto", "Descripcion")
        inc.resolver()
        # Hacemos el test
        self.assertEqual(inc.get_estado(), "Resuelta")