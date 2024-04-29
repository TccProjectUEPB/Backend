from sanic import Blueprint
from src.presenters.controllers import SolicitacaoController
from src.main.request_handlers.sanic_request_handler import sanic_request_handler
from functools import partial


SOLICITACAO_ROUTES = Blueprint("solicitacao")

@SOLICITACAO_ROUTES.route("solicitacoes", methods=["POST"])
async def create_solicitacao(request):
    handler = SolicitacaoController().send
    return await sanic_request_handler(handler, request)


@SOLICITACAO_ROUTES.route("/professores/<professor_id:str>/solicitacoes", methods=["GET"])
async def get_solicitacao_by_prof(request, professor_id):
    handler = partial(SolicitacaoController().get_by_prof, professor_id)
    return await sanic_request_handler(handler, request)

@SOLICITACAO_ROUTES.route("/professores/<professor_id:str>/solicitacoes/<solicitacao_id:str>", methods=["GET"])
async def aswer_solicitacao(request, professor_id: str, solicitacao_id: str):
    handler = partial(SolicitacaoController().update_one, professor_id, solicitacao_id)
    return await sanic_request_handler(handler, request)


@SOLICITACAO_ROUTES.route("/solicitacoes", methods=["GET"])
async def create_solicitacao(request, professor_id):
    handler = partial(SolicitacaoController().send, professor_id)
    return await sanic_request_handler(handler, request)