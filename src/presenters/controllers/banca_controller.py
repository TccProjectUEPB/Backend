from src.application.services import BancaService
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus


class BancaController:
    async def get_one(self, id, request: HttpRequest = None):
        result = await BancaService().get_one(id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def get_all(self, request: HttpRequest = None):
        result = await BancaService().get_all(request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def create(self, id: str, request: HttpRequest):
        result = await BancaService().create(id, request)

        return HttpResponse.build(result, HTTPStatus.CREATED, {})

    async def schedule(self, id: str, request: HttpRequest = None):
        result = await BancaService().schedule(id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def finish(self, id: str, request: HttpRequest = None):
        result = await BancaService().finish(id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})
