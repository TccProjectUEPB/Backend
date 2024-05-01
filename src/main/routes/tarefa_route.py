from sanic import Blueprint
from src.presenters.controllers import TarefaController
from src.main.middlewares import authenticated
from src.main.request_handlers.sanic_request_handler import sanic_request_handler
from functools import partial


TAREFA_ROUTES = Blueprint("tarefa")


@TAREFA_ROUTES.route("/orientacoes/<orientacao_id:str>/tarefas", methods=["GET"])
@authenticated("tf:r")
async def get_tarefas(request, orientacao_id: str):
    request.args["orientation_id"] = [orientacao_id]
    handler = TarefaController().get_all
    return await sanic_request_handler(handler, request)


@TAREFA_ROUTES.route("/orientacoes/<orientacao_id:str>/tarefas", methods=["POST"])
@authenticated("tf:c")
async def create_tarefa(request, orientacao_id: str):
    handler = partial(TarefaController().create, orientacao_id)
    return await sanic_request_handler(handler, request)


@TAREFA_ROUTES.route(
    "/orientacoes/<orientacao_id:str>/tarefas/<tarefa_id:str>", methods=["GET"]
)
@authenticated("tf:r")
async def get_tarefa(request, orientacao_id: str, tarefa_id: str):
    handler = partial(TarefaController().get_one, orientacao_id, tarefa_id)
    return await sanic_request_handler(handler, request)


@TAREFA_ROUTES.route(
    "/orientacoes/<orientacao_id:str>/tarefas/<tarefa_id:str>", methods=["PATCH"]
)
@authenticated("tf:u")
async def update_tarefa(request, orientacao_id: str, tarefa_id: str):
    handler = partial(TarefaController().update_one, orientacao_id, tarefa_id)
    return await sanic_request_handler(handler, request)


@TAREFA_ROUTES.route(
    "/orientacoes/<orientacao_id:str>/tarefas/<tarefa_id:str>", methods=["DELETE"]
)
@authenticated("tf:d")
async def delete_tarefa(request, orientacao_id: str, tarefa_id: str):
    handler = partial(TarefaController().delete_one, orientacao_id, tarefa_id)
    return await sanic_request_handler(handler, request)
