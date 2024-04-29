from sanic import Blueprint
from src.presenters.controllers import SolicitacaoController
from src.main.middlewares import authenticated, admin_or_id
from src.main.request_handlers.sanic_request_handler import sanic_request_handler
from functools import partial


SOLICITACAO_ROUTES = Blueprint("solicitacao")


@SOLICITACAO_ROUTES.route("/solicitacoes", methods=["GET"])
@authenticated("sl:r")
async def get_solicitacoes(request, professor_id):
    handler = partial(SolicitacaoController().get_all, professor_id)
    return await sanic_request_handler(handler, request)


@SOLICITACAO_ROUTES.route("solicitacoes", methods=["POST"])
@authenticated("sl:c")
async def create_solicitacao(request):
    handler = SolicitacaoController().create
    return await sanic_request_handler(handler, request)


@SOLICITACAO_ROUTES.route("/professores/<professor_id:str>/solicitacoes", methods=["GET"])
@authenticated("slp:r")
@admin_or_id("professor_id")
async def get_solicitacao_by_prof(request, professor_id):
    request.args["professor_id"] = [professor_id]
    handler = SolicitacaoController().get_all
    return await sanic_request_handler(handler, request)


@SOLICITACAO_ROUTES.route("/alunos/<aluno_id:str>/solicitacoes", methods=["GET"])
@authenticated("sla:r")
@admin_or_id("aluno_id")
async def get_solicitacao_by_aluno(request, aluno_id):
    request.args["aluno_id"] = [aluno_id]
    handler = SolicitacaoController().get_all
    return await sanic_request_handler(handler, request)


@SOLICITACAO_ROUTES.route("/professores/<professor_id:str>/solicitacoes/<solicitacao_id:str>", methods=["PATCH"])
@authenticated("sl:u")
@admin_or_id("professor_id")
async def answer_solicitacao(request, professor_id: str, solicitacao_id: str):
    handler = partial(SolicitacaoController().update_one, professor_id, solicitacao_id)
    return await sanic_request_handler(handler, request)
