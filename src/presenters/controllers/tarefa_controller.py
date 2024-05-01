from src.application.services import TarefaService
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus


class TarefaController:
    async def create(self, request: HttpRequest):
        result = await TarefaService().create(request)

        return HttpResponse.build(result, HTTPStatus.CREATED, {})

    async def get_one(self, id: str, request: HttpRequest = None):
        result = await TarefaService().get_one(id)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def get_all(self, request: HttpRequest = None):
        result = await TarefaService().get_all(request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def update_one(self, id: str, request: HttpRequest = None):
        result = await TarefaService().update_one(id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def delete_one(self, id: str, request: HttpRequest = None):
        await TarefaService().delete_one(id)

        return HttpResponse.build(None, HTTPStatus.NO_CONTENT, {})
