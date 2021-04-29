class Estado():
    __nome: str
    __sigla: str
    __imagem: str

    def __init__(self, nome: str, sigla: str, imagem: str):
        self.__nome = nome
        self.__sigla = sigla
        self.__imagem = imagem
        self.__noticia_lista = []

    def get_nome(self):
        return self.__nome

    def get_sigla(self):
        return self.__sigla

    def get_imagem(self):
        return self.__imagem

    def get_noticia_lista(self):
        return self.__noticia_lista

    def set_nome(self, nome: str) -> None:
        self.__nome = nome 

    def set_sigla(self):
        self.__sigla = sigla

    def set_imagem(self, imagem: str) -> None:
        self.__imagem = imagem

    def set_noticia_lista(self, noticia_lista: list):
        self.__noticia_lista = noticia_lista

    def adiciona_noticia_lista(self, noticia_lista: list):
        self.__noticia_lista.append(noticia_lista)