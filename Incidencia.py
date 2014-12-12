__author__ = 'Luzu'

class Incidencia:
    def __init__(self,ID,asunto,descripcion):
        self.ID=ID
        self.asunto = asunto
        self.descripcion = descripcion
        self.estado='Abierta'

    def get_ID(self):
        return self.ID

    def get_asunto(self):
        return self.asunto

    def get_descripcion(self):
        return self.descripcion

    def get_estado(self):
        return self.estado

    def set_ID(self,ID):
        self.ID=ID

    def set_asunto(self,asunto):
        self.asunto=asunto

    def set_descripcion(self,descripcion):
        self.descripcion=descripcion

    def resolver(self):
        self.estado='Resuelta'