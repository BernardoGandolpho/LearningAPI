Esse repositório inclui diversos projetos feitos durante meu estudo de APIs utiizando o padrão REST.

Criando o ambiente virtual
$ virtualenv venv -p python3

Ativando o ambiente virtual
$ source venv/bin/activate

Instalaando dependencias
$ pip3 install -r requirements.txt


O primeiro projeto criado fui um código em python para fazer requisições simples com métodos GET e POST utilizando o python.
Para executá-lo, é possível executar o seguinte comando a partir da pasta raíz do projeto:
$ python3 python-requests/main.py


Em seguida, foram montados 3 projetos para testar 3 diferentes frameworks para APIs.
Executar o servidor Flask a partir do diretório frameworks-examples/flask/
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run

Executar o servidor Django a partir do diretório frameworks-examples/django/
$ python3 manage.py runserver

Executar o servidor FastAPI a partir do diretório frameworks-examples/fastapi/
$ uvicorn app:app --reload


A pasta /fastapi no diretório raíz possui um projeto mais elaborado usando o FastAPI.
O arquivo api_practice.py possui um exemplo utilizando modelos e classes importantes do FastAPI e pode ser executado com o comando:
$ uvicorn app_practice:app --reload

Na pasta /pokemon-api está o projeto mais elaborado utilizando o que aprendi para fazer uma API RESTful utilizando FastAPI.
para executá-lo, basta definir a variável de ambiente MONGODB_URL com o link de conexão com um banco de dados MongoDB e executar o comando:
$ python main.py