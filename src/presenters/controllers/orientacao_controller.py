from src.application.domain.models import CreateOrientacaoModel
from src.application.services import OrientacaoService
from src.application.domain.utils import UserTypes, UserScopes
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus


class OrientacaoController:

    async def get_all(self, request: HttpRequest = None):
        result = await OrientacaoService().get_all(request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def get_one_by_prof(self, professor_id: str, orientation_id: str, request: HttpRequest = None):
        result = await OrientacaoService().get_one_by_prof(professor_id, orientation_id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def get_one_by_aluno(self, aluno_id: str, orientation_id: str, request: HttpRequest = None):
        result = await OrientacaoService().get_one_by_aluno(aluno_id, orientation_id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})


    async def update_one(self, professor_id: str, orientation_id: str, request: HttpRequest = None):
        result = await OrientacaoService().update_one(professor_id, orientation_id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})
