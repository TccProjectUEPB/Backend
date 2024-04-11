from src.application.domain.models import AlunoModel
from src.infrastructure.database import get_db
from src.infrastructure.repositories import AlunoRepository
from src.presenters.controllers import AlunoController
#from src.main.middlewares import authenticated
from src.main.request_handlers import sanic_request_handler
from sanic import Blueprint, request, response
from functools import partial


ALUNO = Blueprint("aluno")

@ALUNO.route("/alunos", methods=["GET"])
#@authenticated("al:ra")
async def get_alunos(request: request):
    handler = AlunoController().get_all
    return await sanic_request_handler(
        request=request, api_route=handler
    )

@ALUNO.route("/alunos", methods=["POST"])
#@authenticated("al:c")
async def create_aluno(request: request):
    handler = AlunoController().create
    return await sanic_request_handler(
        request=request, api_route=handler
    )
    

@ALUNO.route("/alunos/<aluno_id:str>", methods=["GET"])
#@authenticated("al:r")
async def get_aluno(request: request, aluno_id: str):
    handler = partial(AlunoController().get_one, aluno_id)
    return await sanic_request_handler(
        request=request, api_route=handler
    )

@ALUNO.route("/alunos/<aluno_id:str>", methods=["PATCH"])
#@authenticated("al:u")
async def update_aluno(request: request, aluno_id: str):
    handler = partial(AlunoController().update_one, aluno_id)
    return await sanic_request_handler(
        request=request, api_route=handler
    )

@ALUNO.route("/alunos/<aluno_id:str>", methods=["DELETE"])
#@authenticated("al:d")
async def delete_aluno(request: request, aluno_id: str):
    handler = partial(AlunoController().delete_one, aluno_id)
    return await sanic_request_handler(
        request=request, api_route=handler
    )