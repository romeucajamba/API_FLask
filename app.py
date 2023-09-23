from flask import Flask
from flask import jsonify
from markupsafe import escape
from flask import request
from flask import json

app = Flask(__name__)

developer = [
    {
        'id': 0,
        'nome': 'Tomás',
        'habilidades':['python', 'flask'],
    },
    {
        'id': 1,
        'nome': 'Cajmaba',
        'habilidades': ['python', 'django']
    },
]

@app.route('/', methods=['GET','PUT', 'DELETE', 'POST'])

def developers():
    if request.method == 'GET':
        try:
            response = developer
        except IndexError:
            response = {'status': 'Erro', 'message': 'Desenvolvedor não existe!'}
        except Exception:
            message = 'Messagem de erro desconhecido, procure o ADM da API'
            staus = 'Erro'
            response = {'status': staus, 'message': message}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        soft = developer
        return jsonify(dados)

    elif request.method == 'DELETE':
        developer.pop()
        return jsonify({'status': 'Sucesso', 'message': 'Registro excluido'})

# Inserir dados e mostrar lista de todos
@app.route('/', methods=['POT', 'GET'])
def lista():
    if request.method == 'POST':
        dados = json.loads(request.data)
        position = len(developer)
        dados[id] = position
        developer.appednd(dados)
        return jsonify(developer)

    elif request.methods == 'GET':
        return jsonify(developer)




if __name__ == '__main__':
    app.run(debug=True)
