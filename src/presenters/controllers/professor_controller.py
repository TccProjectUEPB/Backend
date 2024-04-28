from src.application.services import ProfessorService
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus


class ProfessorController:
    async def create(self, request: HttpRequest):
        result = await ProfessorService().create(request)

        return HttpResponse.build(result, HTTPStatus.CREATED, {})

    async def get_one(self, professor_id: str, request: HttpRequest = None):
        result = await ProfessorService().get_one(professor_id)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def get_all(self, request: HttpRequest = None):
        result = await ProfessorService().get_all(request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def update_one(self, professor_id: str, request: HttpRequest = None):
        result = await ProfessorService().update_one(professor_id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def delete_one(self, professor_id: str, request: HttpRequest = None):
        await ProfessorService().delete_one(professor_id)

        return HttpResponse.build(None, HTTPStatus.NO_CONTENT, {})
