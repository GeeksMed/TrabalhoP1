from application import app
from flask import Flask, render_template, request, url_for
from application.model.dao.estadoDAO import EstadoDAO
from application.model.entity.estado import Estado
from application.model.entity.noticia import noticia

noticia_lista = []

estado_lista = []

estadoDAO = EstadoDAO(estado_lista)

@app.route('/')
def index():
    return render_template("index.html", estado_list = estadoDAO.get_estadoLista())

@app.route('/<nome>')
def estado(nome):
    for estado in estado_lista:
        if estado.get_nome() == nome:
            return render_template("video.html", estado = estado)
    return render_template("index.html", estado_list = estadoDAO.get_estadoLista())
