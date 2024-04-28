from src.application.domain.models import CreateProfessorModel, AuthModel, ProfessorModel, ProfessorQueryModel
from src.application.domain.utils import UserTypes
from src.infrastructure.database import get_db
from src.infrastructure.repositories import ProfessorRepository, AuthRepository
from src.presenters.exception import ConflictException
from src.presenters.helpers import HttpRequest
import bcrypt


class ProfessorService:
    async def get_one(self, id):
        async with get_db() as session:
            repo = ProfessorRepository(session)
            return await repo.get_one(id)

    async def get_all(self, request: HttpRequest):
        query = ProfessorQueryModel(**request.query).query_dict()
        async with get_db() as session:
            repo = ProfessorRepository(session)
            return await repo.get_all(query)

    async def create(self, request: HttpRequest):
        professor = CreateProfessorModel(**request.body)
        result = None
        async with get_db() as session:
            repo = ProfessorRepository(session)
            try:
                result = await repo.create(
                    professor.model_dump(exclude_none=True, exclude={
                                     "id", "username", "matricula", "password"}),
                    commit=False
                )
                professor.password = bcrypt.hashpw(
                    professor.password.encode(), bcrypt.gensalt(13)
                ).decode()
                auth = AuthModel(**{**professor.model_dump(exclude_none=True, exclude={"id"}),
                                    **{
                                        "user_type": UserTypes.PROFESSOR.value,
                                        "refresh_token": None,
                                        "last_login": None,
                                        "foreign_id": str(result["id"]),
                }
                })
                auth_repo = AuthRepository(session)
                await auth_repo.create(auth.model_dump(exclude_none=True), False)
                await session.commit()
                return result
            except BaseException as err:
                await session.rollback()
                raise ConflictException("Already exist", "email/username/matricula already used")

    async def update_one(self, id: str, request: HttpRequest):
        professor = ProfessorModel(**request.body)
        async with get_db() as session:
            repo = ProfessorRepository(session)
            return await repo.update_one(id, professor.model_dump(exclude_none=True))

    async def delete_one(self, id: str):
        async with get_db() as session:
            repo = ProfessorRepository(session)
            await repo.delete_one(id)
