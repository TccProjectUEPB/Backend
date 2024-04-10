from sanic import Sanic
from src.routes import ALUNO

app = Sanic("http")

app.blueprint(ALUNO, version=1)
