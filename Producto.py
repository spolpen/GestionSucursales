# coding=utf-8
__author__ = 'Polo'


class Producto(object):
    """Clase producto

    Define un producto con sus atributos de ID, nombre y precio.

    """

    def __init__(self, ide, nombre, precio):
        """Constructor producto

        Metodo constructor de la clase producto, que inicializa sus atributos con los valores introducidos.

        :param ide:
        :param nombre:
        :param precio:
        :return:
        """
        self.ID = ide
        self.nombre = nombre
        self.precio = precio

    def get_id(self):
        """Get ID

        Metodo que devuelve la ID del producto.

        :return:ID producto
        """
        return self.ID

    def get_nombre(self):
        """Get nombre

        Metodo que devuelve el nombre del producto

        :return:nombre producto
        """
        return self.nombre

    def get_precio(self):
        """Get precio

        Metodo que devuelve el precio del producto

        :return:precio producto
        """
        return self.precio

    def set_id(self, ide):
        """Set ID producto

        Cambia la ID del producto al parametro introducido.

        :param ide:
        :return:
        """
        self.ID = ide

    def set_nombre(self, nombre):
        """Set nombre producto

        Cambia el nombre del producto al parametro introducido.

        :param nombre:
        :return:
        """
        self.nombre = nombre

    def set_precio(self, precio):
        """Set precio producto

        Cambia el precio del producto al parametro introducido.

        :param precio:
        :return:
        """
        self.precio = precio