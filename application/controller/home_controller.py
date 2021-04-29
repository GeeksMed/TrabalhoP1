from application import app
from flask import Flask, render_template, request, url_for
from application.model.dao.estadoDAO import EstadoDAO
from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia

estado_lista = []
estado_lista.append(Estado('Acre', 'AC', '/img/bacre.png')) #0
estado_lista.append(Estado('Alagoas', 'AL', '/img/balagoas.png')) #1
estado_lista.append(Estado('Amapá', 'AP', '/img/bamapa.png')) #2
estado_lista.append(Estado('Amazonas', 'AM', '/img/bamazonas.png')) #3
estado_lista.append(Estado('Bahia', 'BA', '/img/bbahia.png')) #4
estado_lista.append(Estado('Ceará', 'CE', '/img/bceara.png')) #5
estado_lista.append(Estado('Distrito Federal', 'DF', '/img/bdistritofederal.png')) #6
estado_lista.append(Estado('Espirito Santo', 'ES', '/img/bespiritosanto.png')) #7
estado_lista.append(Estado('Goias', 'GO', '/img/bgoias.png')) #8
estado_lista.append(Estado('Maranhão', 'MA', '/img/bmaranhao.png')) #9
estado_lista.append(Estado('Mato Grosso', 'MT', '/img/bmatogrosso.png')) #10
estado_lista.append(Estado('Mato Grosso do Sul', 'MS', '/img/bmatogrossodosul.png')) #11
estado_lista.append(Estado('Minas Gerais', 'MG', '/img/bminasgerais.png')) #12
estado_lista.append(Estado('Pará', 'PA', '/img/bpara.png')) #13
estado_lista.append(Estado('Paraiba', 'PB', '/img/bparaiba.png')) #14
estado_lista.append(Estado('Paraná', 'PR', '/img/bparana.png')) #15
estado_lista.append(Estado('Pernambuco', 'PE', '/img/bpernambuco.png')) #16
estado_lista.append(Estado('Piauí', 'PI', '/img/bpiaui.png')) #17
estado_lista.append(Estado('Rio de Janeiro', 'RJ', '/img/briodejaneiro.png')) #18
estado_lista.append(Estado('Rio Grande do Norte', 'RN', '/img/briograndedonorte.png')) #19
estado_lista.append(Estado('Rio Grande do Sul', 'RS', '/img/briograndedosul.png')) #20
estado_lista.append(Estado('Rondônia', 'RO', '/img/brondonia.png')) #21
estado_lista.append(Estado('Roraima', 'RR', '/img/broraima.png')) #22
estado_lista.append(Estado('Santa Catarina', 'SC', '/img/bsantacatarina.png')) #23
estado_lista.append(Estado('São Paulo', 'SP', '/img/bsaopaulo.png')) #24
estado_lista.append(Estado('Sergipe', 'SE', '/img/bsergipe.png')) #25
estado_lista.append(Estado('Tocantins', 'TO', '/img/btocantins.png')) #26

noticia_lista = []
noticia_lista.append(Noticia("Salvamento de gato", 
    estado_lista[18].get_imagem(), 
    "Gato é salvo em Barra do Piraí, por moradores que estavam passando na rua, enquanto falavam sobre os assaltos do dia anterior.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl nisi scelerisque eu ultrices vitae auctor. Leo duis ut diam quam nulla porttitor massa id. Consectetur lorem donec massa sapien faucibus et molestie ac. Laoreet id donec ultrices tincidunt arcu non. Cras tincidunt lobortis feugiat vivamus at augue. Non curabitur gravida arcu ac tortor dignissim convallis aenean et. Fringilla est ullamcorper eget nulla facilisi. Venenatis lectus magna fringilla urna porttitor rhoncus. Nec ullamcorper sit amet risus. Malesuada fames ac turpis egestas sed tempus urna et pharetra. Nunc mattis enim ut tellus elementum sagittis vitae. Turpis massa tincidunt dui ut ornare lectus. Sapien faucibus et molestie ac feugiat sed."))
noticia_lista.append(Noticia("Salvamento de cachorro", 
    estado_lista[18].get_imagem(), 
    "Cachorro é salvo em Valença, por um bombeiro que passava no local. A vizinhança agradeçe ao herói.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl nisi scelerisque eu ultrices vitae auctor. Leo duis ut diam quam nulla porttitor massa id. Consectetur lorem donec massa sapien faucibus et molestie ac. Laoreet id donec ultrices tincidunt arcu non. Cras tincidunt lobortis feugiat vivamus at augue. Non curabitur gravida arcu ac tortor dignissim convallis aenean et. Fringilla est ullamcorper eget nulla facilisi. Venenatis lectus magna fringilla urna porttitor rhoncus. Nec ullamcorper sit amet risus. Malesuada fames ac turpis egestas sed tempus urna et pharetra. Nunc mattis enim ut tellus elementum sagittis vitae. Turpis massa tincidunt dui ut ornare lectus. Sapien faucibus et molestie ac feugiat sed."))
noticia_lista.append(Noticia("Salvamento de carro no lago", 
    estado_lista[24].get_imagem(), 
    "Carro é encontrado em São Paulo, por um bombeiro que passava no local. A vizinhança informou que o pneu estourou e o carro caiu no Tiete.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl nisi scelerisque eu ultrices vitae auctor. Leo duis ut diam quam nulla porttitor massa id. Consectetur lorem donec massa sapien faucibus et molestie ac. Laoreet id donec ultrices tincidunt arcu non. Cras tincidunt lobortis feugiat vivamus at augue. Non curabitur gravida arcu ac tortor dignissim convallis aenean et. Fringilla est ullamcorper eget nulla facilisi. Venenatis lectus magna fringilla urna porttitor rhoncus. Nec ullamcorper sit amet risus. Malesuada fames ac turpis egestas sed tempus urna et pharetra. Nunc mattis enim ut tellus elementum sagittis vitae. Turpis massa tincidunt dui ut ornare lectus. Sapien faucibus et molestie ac feugiat sed."))
for i in range(0, 27):
    noticia_lista.append(Noticia("Lorem ipsum", 
    estado_lista[i].get_imagem(), 
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl nisi scelerisque eu ultrices vitae auctor. Leo duis ut diam quam nulla porttitor massa id. Consectetur lorem donec massa sapien faucibus et molestie ac. Laoreet id donec ultrices tincidunt arcu non. Cras tincidunt lobortis feugiat vivamus at augue. Non curabitur gravida arcu ac tortor dignissim convallis aenean et. Fringilla est ullamcorper eget nulla facilisi. Venenatis lectus magna fringilla urna porttitor rhoncus. Nec ullamcorper sit amet risus. Malesuada fames ac turpis egestas sed tempus urna et pharetra. Nunc mattis enim ut tellus elementum sagittis vitae. Turpis massa tincidunt dui ut ornare lectus. Sapien faucibus et molestie ac feugiat sed."))

for i in range(3, len(noticia_lista)):
    for j in noticia_lista[i-3:i-2]:
        estado_lista[i-3].adiciona_noticia_lista(j)

for i in noticia_lista[0:2]:
    estado_lista[18].adiciona_noticia_lista(i)

for i in noticia_lista[2:3]:   
    estado_lista[24].adiciona_noticia_lista(i)

estadoDAO = EstadoDAO(estado_lista)

@app.route('/')
def index():
    return render_template("index.html", estado_list = estadoDAO.get_estadoLista())

@app.route('/<titulo>')
def noticia(titulo):
    for noticia in noticia_lista:
        if noticia.get_titulo() == titulo:
            return render_template("noticia.html", noticia = noticia)
    return render_template("index.html", estado_list = estado_lista)

