from datetime import datetime

class Noticia():
    __id: int
    __titulo: str
    __imagem: str
    __descricao: str
    __resumo: str
    __qt_visualizacao: int
    __qt_curtidas: int
    __data_publicacao: str

    def __init__(self, id: int, titulo: str, imagem: str, resumo: str, descricao: str, qt_visualizacao=0, qt_curtidas=0, data_publicacao=str(datetime.now())[0:19]):
        self.__id = id
        self.__titulo = titulo
        self.__imagem = imagem
        self.__descricao = descricao
        self.__resumo = resumo
        self.__qt_visualizacao = qt_visualizacao
        self.__qt_curtidas = qt_curtidas
        self.__data_publicacao = data_publicacao
        
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo
    
    def get_imagem(self):
        return self.__imagem

    def get_descricao(self):
        return self.__descricao

    def get_resumo(self):
        return self.__resumo

    def get_qt_visualizacao(self):
        return self.__qt_visualizacao

    def get_qt_curtidas(self):
        return self.__qt_curtidas

    def get_data_publicacao(self):
        return self.__data_publicacao

    def set_id(self, id: int):
        self.__id = id
        
    def set_titulo(self, titulo: str):
        self.__titulo = titulo
    
    def set_imagem(self, imagem: str):
        self.__imagem = imagem

    def set_descricao(self, descricao: str):
        self.__descricao = descricao 

    def set_resumo(self):
        self.__resumo = resumo
    
    def set_qt_visualizacao(self, qt_visualizacao: str):
        self.__qt_visualizacao = qt_visualizacao

    def set_qt_curtidas(self, qt_curtidas: str):
        self.__qt_curtidas = qt_curtidas

    def set_data_publicacao(self, data_publicacao: str):
        self.__data_publicacao = data_publicacao