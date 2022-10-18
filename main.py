# Importar a classe Flask e o objeto request:
from flask import Flask, request

# Criar o objeto Flask app:
app = Flask(__name__)
# http://127.0.0.1:5000/testes/1?linguagem=Python
@app.route('/testes/1')
def teste_query_string_1_agurmento_get():
linguagem = request.args.get('linguagem')
return '''<h1>Linguagem informada: {}</h1>'''.format(linguagem)
# http://127.0.0.1:5000/testes/2?linguagem=Python&framework=Flask
@app.route('/testes/2')
def teste_query_string_2_agurmentos_get():
linguagem = request.args.get('linguagem')
framework = request.args.get('framework')
return '''<h1>Linguagem informada: {}</h1>

<h1>Framework informado: {}</h1>'''.format(linguagem, framework)

# http://127.0.0.1:5000/testes/3?linguagem=Python&framework=Flask
@app.route('/testes/3')
def teste_query_string_2_agurmentos_vetor():
linguagem = request.args['linguagem']
framework = request.args['framework']
return '''<h1>Linguagem informada: {}</h1>

<h1>Framework informado: {}</h1>'''.format(linguagem, framework)

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
app.run(debug = True, port = 5000)