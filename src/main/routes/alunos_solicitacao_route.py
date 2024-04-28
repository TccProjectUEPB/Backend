from sanic import Blueprint
from src.presenters.controllers import SolicitacaoController
from src.main.request_handlers.sanic_request_handler import sanic_request_handler
from functools import partial


SOLICITACAO_ROUTES = Blueprint("solicitacao")

@SOLICITACAO_ROUTES.route("solicitacoes", methods=["POST"])
async def create_solicitacao(request):
    method = SolicitacaoController().send
    return await sanic_request_handler(method, request)


@SOLICITACAO_ROUTES.route("/professores/<professor_id:str>/solicitacoes", methods=["GET"])
async def get_solicitacao_by_prof(request, professor_id):
    method = partial(SolicitacaoController().get_by_prof, professor_id)
    return await sanic_request_handler(method, request)


@SOLICITACAO_ROUTES.route("/solicitacoes", methods=["GET"])
async def create_solicitacao(request, professor_id):
    method = partial(SolicitacaoController().send, professor_id)
    return await sanic_request_handler(method, request)