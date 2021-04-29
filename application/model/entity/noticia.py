class Noticia():
    __estado: Estado
    __titulo: str
    __descricao: str
    __qt_visualizacao: int
    __qt_curtidas: int
    __data_publicacao: str

    def __init__(self, estado: Estado, titulo: str, descricao: str, qt_visualizacao: int, qt_curtidas: int, data_publicacao: str):
        self.__estado = estado
        self.__titulo = titulo
        self.__descricao = descricao
        self.__qt_visualizacao = qt_visualizacao
        self.__qt_curtidas = qt_curtidas
        self.__data_publicacao = data_publicacao
    
    def get_estado(self):
        return self.__estado

    def get_estado_imagem(self):
        return self.__estado.get_imagem()
        
    def get_titulo(self):
        return self.__titulo

    def get_descricao(self):
        return self.__descricao

    def get_qt_visualizacao(self):
        return self.__qt_visualizacao

    def get_qt_curtidas(self):
        return self.__qt_curtidas

    def get_data_publicacao(self):
        return self.__data_publicacao
    
    def set_estado(self, estado: Estado):
        self.__estado = estado
        
    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_descricao(self, descricao: str):
        self.__descricao = descricao 

    def set_qt_visualizacao(self, qt_visualizacao: str):
        self.__qt_visualizacao = qt_visualizacao

    def set_qt_curtidas(self, qt_curtidas: str):
        self.__qt_curtidas = qt_curtidas

    def set_data_publicacao(self, data_publicacao: str):
        self.__data_publicacao = data_publicacao