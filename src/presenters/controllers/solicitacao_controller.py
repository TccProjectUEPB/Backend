from src.application.domain.models import CreateSolicitacaoModel
from src.application.services import SolicitacaoService
from src.application.domain.utils import UserTypes, UserScopes
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus


class SolicitacaoController:

    async def create(self, request: HttpRequest):
        result = await SolicitacaoService().create(request)

        return HttpResponse.build(result, HTTPStatus.CREATED, {})

    async def get_all(self, request: HttpRequest = None):
        result = await SolicitacaoService().get_all(request)

        return HttpResponse.build(result, HTTPStatus.OK, {})


    async def update_one(self, professor_id: str, solicitacao_id: str, request: HttpRequest = None):
        result = await SolicitacaoService().update_one(professor_id, solicitacao_id, request)

        return HttpResponse.build(result, HTTPStatus.OK, {})
