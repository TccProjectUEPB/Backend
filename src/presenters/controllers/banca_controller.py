from src.application.domain.models import CreateSolicitacaoModel
from src.application.services BancaService
from src.application.domain.utils import UserTypes, UserScopes
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus


class BancaController:

    async def create(self, request: HttpRequest):
        result = await BancaService().create(request)

        return HttpResponse.build(result, HTTPStatus.CREATED, {})

    async def get_all(self, request: HttpRequest = None):
        result = await BancaService().get_all(request)

        return HttpResponse.build(result, HTTPStatus.OK, {})


    async def update_one(self, professor_id: str, solicitacao_id: str, request: HttpRequest = None):
        result = await BancaService().update_one(professor_id, solicitacao_id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})
