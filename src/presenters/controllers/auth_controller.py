from src.application.domain.models import CredentialModel
from src.application.domain.utils import UserTypes
from src.infrastructure.database import get_db
from src.infrastructure.repositories import AuthRepository, AuthRepository
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus
import bcrypt


class AuthController:
    async def login(self, request: HttpRequest = None):
        data = CredentialModel(**request.body)

        result = None
        async with get_db() as session:
            repo = AuthRepository(session)
            if data.login.isdigit():
                repo.get_one_by_matricula(data.login)
            else:
                repo.get_one_by_username(data.login)
            result = await repo.update_one(aluno_id, aluno.model_dump(exclude_none=True))
        return HttpResponse.build(result, HTTPStatus.OK, {})

