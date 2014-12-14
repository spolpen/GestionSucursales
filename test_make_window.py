from unittest import TestCase
from Tkinter import *
from Interfaz import *
__author__ = 'Polo'


class TestMakeWindow(TestCase):
    """Clase TestMake_window

    Esta clase crea una ventana de prueba para poder hacer uso de la interfaz grafica.
    De este modo nos es posible testear dicha interfaz y asegurarnos de que el coverage es de 100%.

    """
    def test_make_window(self):
        win2 = make_window()
        set_select_sucursal()
        win2.mainloop()