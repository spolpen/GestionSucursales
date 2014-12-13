from unittest import TestCase
from Incidencia import *
__author__ = 'Polo'


class TestIncidencia(TestCase):
    def test_resolver(self):
        inc = Incidencia(1,"Asunto","Descripcion")
        inc.resolver()
        #Hacemos el test
        self.assertEqual(inc.get_estado(), "Resuelta")