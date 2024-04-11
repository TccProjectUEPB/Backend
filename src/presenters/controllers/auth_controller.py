from src.application.domain.models import CredentialModel
from src.application.domain.utils import UserTypes, UserScopes
from src.infrastructure.database import get_db
from src.infrastructure.repositories import AuthRepository, AuthRepository
from src.presenters.helpers import HttpRequest, HttpResponse
from src.utils import settings, default
from http import HTTPStatus
from datetime import datetime, timedelta
import bcrypt, jwt


class AuthController:
    def getScopeByUserType(self, type: str):
        try:
            UserTypes(type)
            return UserScopes[type.upper()].value
        except ValueError:
            raise Exception("event not listed in events")

    async def login(self, request: HttpRequest = None):
        data = CredentialModel(**request.body)

        response = None
        async with get_db() as session:
            repo = AuthRepository(session)
            result = None
            if data.login.isdigit():
                result = await repo.get_one_by_matricula(data.login)
            else:
                result = await repo.get_one_by_username(data.login)
            if result is not None:
                result = result[0]
                #result = await repo.update_one(aluno_id, aluno.model_dump(exclude_none=True))
                if not bcrypt.checkpw(data.password.encode(), result.password.encode()):
                    return HttpResponse.build(None, HTTPStatus.UNAUTHORIZED, {})
                current = datetime.utcnow()
                token = jwt.encode(
                    {
                        "sub": str(result.foreign_id),
                        "iss": settings.ISSUER,
                        "type": result.user_type,
                        "iat": current,
                        "scope": str(self.getScopeByUserType(result.user_type)),
                        "exp": current + timedelta(seconds=default.TOKEN_EXP_TIME),
                    },
                    settings.JWT_SECRET,
                )
                response = {"access_token": token,
                            "refresh_token": bcrypt.hashpw(token.encode("utf8"), bcrypt.gensalt(12)).decode("utf8")
                }
                await repo.update_one(str(result.id), {"refresh_token": response["refresh_token"], "last_login": datetime.now()})
        return HttpResponse.build(response, HTTPStatus.OK, {})

