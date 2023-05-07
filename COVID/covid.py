import json

import requests
from flask import Flask, render_template, request

app = Flask(__name__)


# window = webview.create_window('Covid-19!', app,  width=1000, height=800,
#                               confirm_close=True)

@app.route('/', methods=['GET'])
def index():
    response = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp')
    dados = json.loads(response.text)

    uf = ["uf"]
    estado = ["state"]
    infectados = ["cases"]
    mortos = ["deaths"]
    suspeitos = ["suspects"]
    descartados = ["refuses"]
    data = ["datetime"]

    return render_template('index.html', dados=dados, uf=uf, estado=estado,
                           infectados=infectados, mortos=mortos,
                           suspeitos=suspeitos, descartados=descartados, data=data)


@app.route("/", methods=['GET', 'POST'])
def index2():
    select = request.form.get('comp_select')
    url = ('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(select))
    headers = {}

    response = requests.request('GET', url, headers=headers)
    dados = json.loads(response.text)

    uf = ["uf"]
    estado = ["state"]
    infectados = ["cases"]
    mortos = ["deaths"]
    suspeitos = ["suspects"]
    descartados = ["refuses"]
    data = ["datetime"]

    return render_template('index.html', dados=dados, uf=uf, estado=estado,
                           infectados=infectados, mortos=mortos,
                           suspeitos=suspeitos, descartados=descartados, data=data)


if __name__ == '__main__':
    app.run(debug=True)
#  webview.start()
