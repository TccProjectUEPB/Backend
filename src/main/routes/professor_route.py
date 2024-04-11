from src.application.domain.models import ProfessorModel
from src.infrastructure.database import get_db
from src.infrastructure.repositories import ProfessorRepository
from src.presenters.controllers import ProfessorController
#from src.main.middlewares import authenticated
from src.main.request_handlers import sanic_request_handler
from sanic import Blueprint, request, response
from functools import partial


PROFESSOR = Blueprint("professor")

@PROFESSOR.route("/professores", methods=["GET"])
#@authenticated("al:ra")
async def get_professors(request: request):
    handler = ProfessorController().get_all
    return await sanic_request_handler(
        request=request, api_route=handler
    )

@PROFESSOR.route("/professores", methods=["POST"])
#@authenticated("al:c")
async def create_professor(request: request):
    handler = ProfessorController().create
    return await sanic_request_handler(
        request=request, api_route=handler
    )
    

@PROFESSOR.route("/professores/<professor_id:str>", methods=["GET"])
#@authenticated("al:r")
async def get_professor(request: request, professor_id: str):
    handler = partial(ProfessorController().get_one, professor_id)
    return await sanic_request_handler(
        request=request, api_route=handler
    )

@PROFESSOR.route("/professores/<professor_id:str>", methods=["PATCH"])
#@authenticated("al:u")
async def update_professor(request: request, professor_id: str):
    handler = partial(ProfessorController().update_one, professor_id)
    return await sanic_request_handler(
        request=request, api_route=handler
    )

@PROFESSOR.route("/professores/<professor_id:str>", methods=["DELETE"])
#@authenticated("al:d")
async def delete_professor(request: request, professor_id: str):
    handler = partial(ProfessorController().delete_one, professor_id)
    return await sanic_request_handler(
        request=request, api_route=handler
    )