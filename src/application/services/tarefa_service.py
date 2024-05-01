from src.application.domain.models import (
    CreateTarefaModel,
    UpdateTarefaModel,
    TarefaQueryModel,
)
from src.application.domain.utils import OrientationType
from src.infrastructure.database import get_db
from src.infrastructure.repositories import (
    OrientacaoRepository,
    TarefaRepository,
)
from src.presenters.exception import ConflictException
from src.presenters.helpers import HttpRequest


class TarefaService:
    async def get_one(self, related_id: str, id: str, request: HttpRequest):
        async with get_db() as session:
            repo = TarefaRepository(session)
            return await repo.get_one(id)

    async def get_all(self, request: HttpRequest):
        query = TarefaQueryModel(**request.query).query_dict()
        async with get_db() as session:
            repo = TarefaRepository(session)
            return await repo.get_all(query)

    async def create(self, related_id: str, id: str, request: HttpRequest):
        banca = CreateTarefaModel(id=id, orientation_id=related_id)
        async with get_db() as session:
            repo = TarefaRepository(session)
            orientation_repo = OrientacaoRepository(session)
            orientation = await orientation_repo.get_one(related_id)
            if not orientation:
                raise ConflictException("It does not exists", "Entity does not exists")
            if orientation["status"] != OrientationType.EM_ANDAMENTO.value:
                raise ConflictException(
                    "Invalid state", "Entity is on an invalid state"
                )
            try:
                return await repo.create(banca.model_dump(exclude_none=True))
            except BaseException as err:
                await session.rollback()
                raise err

    async def update(self, related_id: str, id: str, request: HttpRequest):
        banca = UpdateTarefaModel(**request.body)
        async with get_db() as session:
            repo = TarefaRepository(session)
            orientation_repo = OrientacaoRepository(session)
            orientation = await orientation_repo.get_one(related_id)
            if not orientation:
                raise ConflictException("It does not exists", "Entity does not exists")
            if orientation["status"] != OrientationType.EM_BANCA.value:
                raise ConflictException(
                    "Invalid state", "Entity is on an invalid state"
                )
            try:
                result = await repo.update_one(id, banca.model_dump(exclude_none=True))
                await session.commit()
                return result
            except BaseException as err:
                await session.rollback()
                raise err

    async def delete_one(self, id: str):
        async with get_db() as session:
            repo = TarefaRepository(session)
            await repo.delete_one(id)
