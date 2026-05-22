import random
from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

@routes.route('/') #define a rota para a página inicial da aplicação.
def homepage(): #define a função que será executada quando a rota for acessada. Essa função renderiza o template 'homepage.html' e o retorna como resposta para o cliente.
    return render_template('homepage.html')#render_template é uma função do Flask que renderiza um template HTML e o retorna como resposta para o cliente. O template 'homepage.html' deve estar localizado na pasta 'templates' do projeto.


@routes.route('/pagina2', methods=['GET', 'POST'])
def pagina2():
    resultado = None
    n1 = random.randint(1, 10)#gera um número aleatório entre 1 e 10 para n1.
    n2 = random.randint(1, 10)#gera um número aleatório entre 1 e 10 para n2.
    operacao = random.choice(['+', '-', '*','/'])#seleciona aleatoriamente uma operação entre adição, subtração, multiplicação e divisão para a variável operacao.

    resposta_correta = None #inicializa a variável resposta_correta como None. Essa variável será usada para armazenar a resposta correta com base na operação selecionada.

    if request.method == 'POST': #verifica se o método da requisição é POST, o que indica que o formulário foi enviado. Se for POST, o código dentro desse bloco será executado para processar os dados do formulário.
        n1 = int(request.form.get('n1')) #obtém o valor de n1 do formulário enviado pelo usuário, converte-o para um inteiro e o armazena na variável n1.
        n2 = int(request.form.get('n2')) 
        operacao = request.form.get('operacao') #obtém o valor da operação selecionada pelo usuário no formulário e o armazena na variável operacao.
        resposta_usuario = int(request.form.get('resposta')) #obtém a resposta fornecida pelo usuário no formulário, converte-a para um inteiro e a armazena na variável resposta_usuario.

        if operacao == '+':
            resposta_correta = n1 + n2
        elif operacao == '-':
            resposta_correta = n1 - n2
        elif operacao == '*':
            resposta_correta = n1 * n2
        elif operacao == '/':
            resposta_correta = n1 / n2

        if resposta_usuario == resposta_correta:
            resultado = "✅ Parabéns! Você acertou!"
        else:
            resultado = f"❌ Errou! A resposta era {resposta_correta}"

        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        operacao = random.choice(['+', '-', '*', '/'])

    return render_template('homepageII.html',
                           n1=n1, n2=n2,
                           operacao=operacao,
                           resultado=resultado)