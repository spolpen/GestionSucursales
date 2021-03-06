# coding=utf-8
__author__ = 'Luzu'


class Incidencia:
    """Clase incidencia

    Esta clase representa una incidencia de la sucursal y automaticamente se inicializa
    como "Abierta" pudiendo resolverse mediante la interfaz de usuario.

    """

    def __init__(self, id_inc, asunto, descripcion):
        """Constructor incidencia

        Metodo constructor de la clase incidencia, que inicializa sus atributos con los parametros introducidos y
        estado en "Abierta".

        :param id_inc:
        :param asunto:
        :param descripcion:
        :return:
        """
        self.id_inc = id_inc
        self.asunto = asunto
        self.descripcion = descripcion
        self.estado = 'Abierta'

    def get_id(self):
        """Get ID incidencia

        Metodo que devuelve la ID de la incidencia.

        :return:ID incidencia
        """
        return self.id_inc

    def get_asunto(self):
        """Get asunto incidencia

        Metodo que devuelve el asunto de la incidencia.

        :return:asunto incidencia
        """
        return self.asunto

    def get_descripcion(self):
        """Get descripcion incidencia

        Metodo que devuelve la descripcion de la incidencia.

        :return:descripcion incidencia
        """
        return self.descripcion

    def get_estado(self):
        """Get estado incidencia

        Metodo que devuelve el estado de la incidencia.

        :return:estado incidencia
        """
        return self.estado

    def set_id(self, id_inc):
        """Set ID incidencia

        Metodo que cambia la ID de la incidencia al parametro introducido.

        :param id_inc:
        :return:
        """
        self.id_inc = id_inc

    def set_asunto(self, asunto):
        """Set asunto incidencia

        Metodo que cambia el asunto de la incidencia al parametro introducido.

        :param asunto:
        :return:
        """
        self.asunto = asunto

    def set_descripcion(self, descripcion):
        """Set descripcion incidencia

        Metodo que cambia la descripcion de la incidencia al parametro introducido.

        :param descripcion:
        :return:
        """
        self.descripcion = descripcion

    def resolver(self):
        """Resolver incidencia

        Metodo que cambia el estado de una incidencia a "Resuelta".

        :return:
        """
        self.estado = 'Resuelta'