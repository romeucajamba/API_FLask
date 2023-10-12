from flask import Flask
from flask import redirect
from flask import url_for

application = Flask(__name__)

@application.route("/formulario/<nome>")
def form(nome):
    return f"""
                <h1> Faça o cadastro {nome} </h1>
                <from>
                    <label>Nome</label>
                    <input type='text' name='name' placeholder='Insira teu nome de usuário'/>
                    <input type='email' name='email' placeholder='Insera o seu email' />
                    <button>Enviar</button>
                </form>
            """.format(nome)

@application.route("/blog/<int:postId>")
def blogue(postId=1):
    if postId >= 0:
        return f"""
                   <p> Informações do Blogue {postId}</p>
                """.format(postId)
    else:
        return "<p>Bolgue de todos</p>"

@application.route("/admin")

def rotas1():
    return "<h1>Rota1</h1>"

@application.route("/rota2/<rota2>")
def rota2(rota2):
    return "<h2>Rota2</h2> {}".format(rota2)

@application.route("/")
def vazio():
    return '<p>Não reconhecido/não faz-se presente no sistema ou BD</p>'

@application.route("/google")
def google():
    return redirect('http://google.com')

@application.route("/user/<name>")
def user(name):
    if name == 'admin':
        return redirect('admin')
    elif name == '':
        return redirect(url_for('vazio'))
    elif name == 'google':
        return redirect(url_for('google'))
    else:
        return redirect(url_for('rota2', rota2 = name))

if __name__ == '__main__':
    application.run(debug=True, port=3000)