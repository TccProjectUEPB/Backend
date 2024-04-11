from sanic import Blueprint
from src.presenters.controllers import AuthController
from src.main.request_handlers.sanic_request_handler import sanic_request_handler


AUTH_ROUTES = Blueprint("auth")

@AUTH_ROUTES.route("/auth", methods=["POST"])
async def auth(request):
    method = AuthController().login
    return await sanic_request_handler(method, request)
