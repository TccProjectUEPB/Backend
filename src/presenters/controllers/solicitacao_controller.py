from src.application.domain.models import CredentialModel
from src.application.domain.utils import UserTypes, UserScopes
from src.infrastructure.repositories import SolicitacaoRepository
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus


class SolicitacaoController:

    async def send(self, request: HttpRequest):
        result = await SolicitacaoRepository().create(request)

        return HttpResponse.build(result, HTTPStatus.CREATED, {})

    async def get_by_prof(self, professor_id: str, request: HttpRequest = None):
        result = await SolicitacaoRepository().get_by_prof(professor_id)

        return HttpResponse.build(result, HTTPStatus.OK, {})
