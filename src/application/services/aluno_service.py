from src.application.domain.models import (
    CreateAlunoModel,
    AuthModel,
    AlunoModel,
    AlunoQueryModel,
)
from src.application.domain.utils import UserTypes
from src.infrastructure.database import get_db
from src.infrastructure.repositories import AlunoRepository, AuthRepository
from src.presenters.exception import ConflictException
from src.presenters.helpers import HttpRequest
import bcrypt


class AlunoService:
    async def get_one(self, id):
        async with get_db() as session:
            repo = AlunoRepository(session)
            return await repo.get_one(id)

    async def get_all(self, request: HttpRequest):
        query = AlunoQueryModel(**request.query).query_dict()
        async with get_db() as session:
            repo = AlunoRepository(session)
            return await repo.get_all(query)

    async def create(self, request: HttpRequest):
        aluno = CreateAlunoModel(**request.body)
        result = None
        async with get_db() as session:
            repo = AlunoRepository(session)
            try:
                result = await repo.create(
                    aluno.model_dump(
                        exclude_none=True,
                        exclude={"id", "username", "matricula", "password"},
                    ),
                    commit=False,
                )
                aluno.password = bcrypt.hashpw(
                    aluno.password.encode(), bcrypt.gensalt(13)
                ).decode()
                auth = AuthModel(
                    **{
                        **aluno.model_dump(exclude_none=True, exclude={"id"}),
                        **{
                            "user_type": UserTypes.ALUNO.value,
                            "refresh_token": None,
                            "last_login": None,
                            "foreign_id": str(result["id"]),
                        },
                    }
                )
                auth_repo = AuthRepository(session)
                await auth_repo.create(auth.model_dump(exclude_none=True), False)
                await session.commit()
                return result
            except BaseException:
                await session.rollback()
                raise ConflictException(
                    "Already exist", "email/username/matricula already used"
                )

    async def update_one(self, id: str, request: HttpRequest):
        aluno = AlunoModel(**request.body)
        async with get_db() as session:
            repo = AlunoRepository(session)
            return await repo.update_one(id, aluno.model_dump(exclude_none=True))

    async def delete_one(self, id: str):
        async with get_db() as session:
            repo = AlunoRepository(session)
            await repo.delete_one(id)
