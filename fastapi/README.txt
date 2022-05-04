Ativando ambiente virtual
$ source venv/bin/activate

Executando a aplicação
$ uvicorn main:app --reload
    * main -> main.py
    * app -> app = FastAPI()
    * --reload -> reload after code changes