from src.application.domain.models import CreateAlunoModel, AuthModel, AlunoModel, AlunoQueryModel
from src.application.domain.utils import UserTypes
from src.infrastructure.database import get_db
from src.infrastructure.repositories import AlunoRepository, AuthRepository
from src.presenters.helpers import HttpRequest, HttpResponse
from http import HTTPStatus
import bcrypt


class AlunoController:
    async def create(self, request: HttpRequest):
        aluno = CreateAlunoModel(**request.body)
        result = None
        async with get_db() as session:
            repo = AlunoRepository(session)
            try:
                result = await repo.create(
                    aluno.model_dump(exclude_none=True, exclude={
                                     "id", "username", "matricula", "password"}),
                    commit=False
                )
                aluno.password = bcrypt.hashpw(
                    aluno.password.encode(), bcrypt.gensalt(13)
                ).decode()
                auth = AuthModel(**{**aluno.model_dump(exclude_none=True, exclude={"id"}),
                                    **{
                                        "user_type": UserTypes.ALUNO.value,
                                        "refresh_token": None,
                                        "last_login": None,
                                        "foreign_id": str(result["id"]),
                }
                })
                auth_repo = AuthRepository(session)
                await auth_repo.create(auth.model_dump(exclude_none=True), False)
                await session.commit()
            except BaseException as err:
                await session.rollback()
                return HttpResponse.build("Already exist", HTTPStatus.CONFLICT, {})
        return HttpResponse.build(result, HTTPStatus.CREATED, {})

    async def get_one(self, aluno_id: str, request: HttpRequest = None):
        result = None
        async with get_db() as session:
            repo = AlunoRepository(session)
            result = await repo.get_one(aluno_id)
        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def get_all(self, request: HttpRequest = None):
        query = AlunoQueryModel(**request.query).query_dict()
        result = None
        async with get_db() as session:
            repo = AlunoRepository(session)
            result = await repo.get_all(query)
        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def update_one(self, aluno_id: str, request: HttpRequest = None):
        aluno = AlunoModel(**request.body)
        result = None
        async with get_db() as session:
            repo = AlunoRepository(session)
            result = await repo.update_one(aluno_id, aluno.model_dump(exclude_none=True))
        return HttpResponse.build(result, HTTPStatus.OK, {})

    async def delete_one(self, aluno_id: str, request: HttpRequest):
        async with get_db() as session:
            repo = AlunoRepository(session)
            await repo.delete_one(aluno_id)
        return HttpResponse.build(None, HTTPStatus.NO_CONTENT, {})
