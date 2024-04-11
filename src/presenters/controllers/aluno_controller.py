from src.application.services import AlunoService
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus


class AlunoController:
    async def create(self, request: HttpRequest):
        result = await AlunoService().create(request)

        return HttpResponse.build(result, HTTPStatus.CREATED, {})

    async def get_one(self, aluno_id: str, request: HttpRequest = None):
        result = await AlunoService().get_one(aluno_id)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def get_all(self, request: HttpRequest = None):
        result = await AlunoService().get_all(request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def update_one(self, aluno_id: str, request: HttpRequest = None):
        result = await AlunoService().update_one(aluno_id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def delete_one(self, aluno_id: str, request: HttpRequest = None):
        await AlunoService().delete_one(aluno_id)

        return HttpResponse.build(None, HTTPStatus.NO_CONTENT, {})
