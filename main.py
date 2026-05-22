from flask import Flask #importa a classe Flask do módulo flask para criar a aplicação web.
from route import routes   # 👈 importa o Blueprint corretamente


app = Flask(__name__)
app.register_blueprint(routes)


if __name__ == '__main__':
    app.run(debug=True) #verifica se o script está sendo executado diretamente e, em caso afirmativo, inicia o servidor de desenvolvimento do Flask com o modo de depuração ativado.

app.run()
