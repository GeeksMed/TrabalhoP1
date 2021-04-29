class Estado():
    __nome: str
    __imagem: str

    def __init__(self, nome: str, imagem: str):
        self.__nome = nome
        self.__imagem = imagem
        self.__noticia_lista = []
    
    def __init__(self, nome: str, imagem: str, noticia_lista: list):
        self.__nome = nome
        self.__imagem = imagem
        self.__noticia_lista = noticia_lista

    def get_nome(self):
        return self.__descricao

    def get_imagem(self):
        return self.__imagem

    def get_noticia_lista(self):
        return self.__noticia_lista

    def set_nome(self, descricao: str) -> None:
        self.__descricao = descricao 

    def set_imagem(self, imagem: str) -> None:
        self.__imagem = imagem

    def set_noticia_lista(self, noticia_lista: list):
        self.__noticia_lista = noticia_lista