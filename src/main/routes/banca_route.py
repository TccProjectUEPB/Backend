from sanic import Blueprint
from src.presenters.controllers import BancaController
from src.main.middlewares import authenticated
from src.main.request_handlers.sanic_request_handler import sanic_request_handler
from functools import partial


BANCA_ROUTES = Blueprint("banca")


@BANCA_ROUTES.route("/bancas", methods=["GET"])
@authenticated("bc:ra")
async def get_bancas(request):
    handler = BancaController().get_all
    return await sanic_request_handler(handler, request)


@BANCA_ROUTES.route("/bancas/<banca_id:str>", methods=["GET"])
@authenticated("bc:r")
async def get_banca(request, banca_id):
    handler = partial(BancaController().get_one, banca_id)
    return await sanic_request_handler(handler, request)


@BANCA_ROUTES.route("bancas/<banca_id:str>", methods=["POST"])
@authenticated("bc:c")
async def create_banca(request, banca_id: str):
    handler = partial(BancaController().create, banca_id)
    return await sanic_request_handler(handler, request)


@BANCA_ROUTES.route("bancas/<banca_id:str>/agendar", methods=["POST"])
@authenticated("bc:s")
async def schedule_banca(request, banca_id: str):
    handler = partial(BancaController().schedule, banca_id)
    return await sanic_request_handler(handler, request)


@BANCA_ROUTES.route("bancas/<banca_id:str>/realizar", methods=["POST"])
@authenticated("bc:fn")
async def finish_banca(request, banca_id: str):
    handler = partial(BancaController().finish, banca_id)
    return await sanic_request_handler(handler, request)
