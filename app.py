from flask import Flask
from flask import jsonify
from flask import json
from flask import request
# jsonify permite returnar os dados em formato JSON

app = Flask(__name__)

@app.route('/')

def firs_aplication():
    return jsonify({'id': 1, 'nome': 'Romeu', 'cargo': 'Developer', 'email': 'romeucajamba@gmail.com', 'empresa': 'ApeixomCode'})


if __name__ == '__main__':
    app.run()