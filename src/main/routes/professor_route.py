from src.presenters.controllers import ProfessorController
from src.main.middlewares import authenticated, admin_or_id
from src.main.request_handlers import sanic_request_handler
from sanic import Blueprint, request
from functools import partial


PROFESSOR = Blueprint("professor")


@PROFESSOR.route("/professores", methods=["GET"])
@authenticated("pf:ra")
async def get_professors(request: request):
    handler = ProfessorController().get_all
    return await sanic_request_handler(
        request=request, api_route=handler
    )


@PROFESSOR.route("/professores/available", methods=["GET"])
@authenticated("pf:avr")
async def create_professor(request: request):
    request.args["available"] = ["true"]
    handler = ProfessorController().get_all
    return await sanic_request_handler(
        request=request, api_route=handler
    )


@PROFESSOR.route("/professores", methods=["POST"])
@authenticated("pf:c")
async def create_professor(request: request):
    handler = ProfessorController().create
    return await sanic_request_handler(
        request=request, api_route=handler
    )


@PROFESSOR.route("/professores/<professor_id:str>", methods=["GET"])
@authenticated("pf:r")
async def get_professor(request: request, professor_id: str):
    handler = partial(ProfessorController().get_one, professor_id)
    return await sanic_request_handler(
        request=request, api_route=handler
    )


@PROFESSOR.route("/professores/<professor_id:str>", methods=["PATCH"])
@authenticated("pf:u")
@admin_or_id("professor_id")
async def update_professor(request: request, professor_id: str):
    handler = partial(ProfessorController().update_one, professor_id)
    return await sanic_request_handler(
        request=request, api_route=handler
    )


@PROFESSOR.route("/professores/<professor_id:str>", methods=["DELETE"])
@authenticated("pf:d")
@admin_or_id("professor_id")
async def delete_professor(request: request, professor_id: str):
    handler = partial(ProfessorController().delete_one, professor_id)
    return await sanic_request_handler(
        request=request, api_route=handler
    )
