from application.model.entity.estado import Estado

class EstadoDAO():

    def __init__(self, estadoLista):
        self.__estadoLista = estadoLista

    def get_estadoLista(self) -> list:
        return self.__estadoLista
