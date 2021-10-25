from flask import Flask,json,request
from flask.json import jsonify


app = Flask(__name__)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Pedro',
        'habilidades':['Python','Flask','JavaScript']
    },
    {
        'id':'1',
        'nome':'Felipe',
        'habilidades':['Python','Django']
    },
    {
        'id':'2',
        'nome':'Gabriel',
        'habilidades':['HTML5,Javascript']
    }
]

#devolve um desenvolvedor pelo id, tambem altera e deleta um desenvolvedor.
@app.route("/dev/<int:id>/", methods=["GET","PUT"])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor do ID {} nao existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. procure o admistrador da API'
            response = {'status':'erro','mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return  jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluido'})

#lista todos os desenvolvedores e inclui um novo desenvolvedor
@app.route('/dev/', methods=['POST','GET'])
def listaDesenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({desenvolvedores[posicao]})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
    
if __name__ == '__main__':
    app.run()