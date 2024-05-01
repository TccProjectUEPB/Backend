from sanic import Blueprint
from src.presenters.controllers import OrientacaoController
from src.main.middlewares import authenticated, admin_or_id
from src.main.request_handlers.sanic_request_handler import sanic_request_handler
from functools import partial


ORIENTACAO_ROUTES = Blueprint("orientacao")


@ORIENTACAO_ROUTES.route("/orientacoes", methods=["GET"])
@authenticated("sl:ra")
async def get_orientacoes(request):
    handler = OrientacaoController().get_all
    return await sanic_request_handler(handler, request)


@ORIENTACAO_ROUTES.route("/professores/<professor_id:str>/orientacoes", methods=["GET"])
@authenticated("orp:r")
@admin_or_id("professor_id")
async def get_orientacoes_by_prof(request, professor_id: str):
    request.args["professor_id"] = [professor_id]
    handler = OrientacaoController().get_all
    return await sanic_request_handler(handler, request)


@ORIENTACAO_ROUTES.route(
    "/professores/<professor_id:str>/orientacoes/<orientacao_id:str>", methods=["GET"]
)
@authenticated("orp:r")
@admin_or_id("professor_id")
async def get_orientacao_by_prof(request, professor_id: str, orientacao_id: str):
    handler = partial(
        OrientacaoController().get_one_by_prof, professor_id, orientacao_id
    )
    return await sanic_request_handler(handler, request)


@ORIENTACAO_ROUTES.route(
    "/professores/<professor_id:str>/orientacoes/<orientacao_id:str>", methods=["PATCH"]
)
@authenticated("orp:u")
@admin_or_id("professor_id")
async def update_orientacao_by_prof(request, professor_id: str, orientacao_id: str):
    handler = partial(OrientacaoController().update_one, professor_id, orientacao_id)
    return await sanic_request_handler(handler, request)


@ORIENTACAO_ROUTES.route("/alunos/<aluno_id:str>/orientacoes", methods=["GET"])
@authenticated("ora:r")
@admin_or_id("aluno_id")
async def get_orientacoes_by_aluno(request, aluno_id: str):
    request.args["aluno_id"] = [aluno_id]
    handler = OrientacaoController().get_all
    return await sanic_request_handler(handler, request)


@ORIENTACAO_ROUTES.route(
    "/alunos/<aluno_id:str>/orientacoes/<orientacao_id:str>", methods=["GET"]
)
@authenticated("ora:r")
@admin_or_id("aluno_id")
async def get_orientacao_by_aluno(request, aluno_id: str, orientacao_id: str):
    handler = partial(OrientacaoController().get_one_by_aluno, aluno_id, orientacao_id)
    return await sanic_request_handler(handler, request)
