from src.application.domain.models import (
    CreateBancaModel,
    ScheduleBancaModel,
    FinishBancaModel,
    BancaQueryModel,
)
from src.application.domain.utils import OrientationType
from src.infrastructure.database import get_db
from src.infrastructure.repositories import (
    OrientacaoRepository,
    BancaRepository,
)
from src.presenters.exception import ConflictException
from src.presenters.helpers import HttpRequest


class BancaService:
    async def get_one(self, id: str, request: HttpRequest):
        async with get_db() as session:
            repo = BancaRepository(session)
            return await repo.get_one(id)

    async def get_all(self, request: HttpRequest):
        query = BancaQueryModel(**request.query).query_dict()
        async with get_db() as session:
            repo = BancaRepository(session)
            return await repo.get_all(query)

    async def create(self, id, request: HttpRequest):
        banca = CreateBancaModel()
        async with get_db() as session:
            repo = BancaRepository(session)
            orientation_repo = OrientacaoRepository(session)
            orientation = await orientation_repo.get_one(id)
            if not orientation:
                raise ConflictException("It does not exists", "Entity does not exists")
            if orientation["status"] != OrientationType.EM_ANDAMENTO.value:
                raise ConflictException(
                    "Invalid state", "Entity is on an invalid state"
                )
            try:
                await repo.create(id, banca.model_dump(exclude_none=True), commit=False)
                await orientation_repo.update_one(
                    id, {"status": OrientationType.EM_BANCA.value}
                )
            except BaseException as err:
                await session.rollback()
                raise err

    async def schedule(self, id: str, request: HttpRequest):
        banca = ScheduleBancaModel(**request.body)
        async with get_db() as session:
            repo = BancaRepository(session)
            return await repo.update_one(
                id, banca.model_dump(exclude_none=True), commit=False
            )

    async def finish(self, id: str, request: HttpRequest):
        banca = FinishBancaModel(**request.body)
        async with get_db() as session:
            repo = BancaRepository(session)
            return await repo.update_one(
                id, banca.model_dump(exclude_none=True), commit=False
            )

    async def delete_one(self, id: str):
        async with get_db() as session:
            repo = BancaRepository(session)
            await repo.delete_one(id)
