from unittest import TestCase
from Tkinter import *
from Interfaz import *
__author__ = 'Polo'


class TestMakeWindow(TestCase):
    """Clase TestMake_window

    Esta clase crea una ventana de prueba para que el usuario interactue con la aplicacion y poder acceder a los metodos
    mediante el coverage

    """
    def test_make_window(self):
        win2 = make_window()
        set_select_sucursal()
        win2.mainloop()