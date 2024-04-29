from src.application.domain.models import UpdateBancaModel, BancaQueryModel
from src.infrastructure.database import get_db
from src.infrastructure.repositories import (
    BancaRepository,
)
from src.presenters.helpers import HttpRequest


class BancaService:
    async def get_one(self, id: str, request: HttpRequest):
        async with get_db() as session:
            repo = BancaRepository(session)
            result = await repo.get_one(id)
            return result

    async def get_all(self, request: HttpRequest):
        query = BancaQueryModel(**request.query).query_dict()
        async with get_db() as session:
            repo = BancaRepository(session)
            return await repo.get_all(query)

    async def update_one(self, id: str, request: HttpRequest):
        orientation = UpdateBancaModel(**request.body)
        async with get_db() as session:
            repo = BancaRepository(session)
            return await repo.update_one(id, orientation.model_dump(
                    exclude_none=True), commit=False)

    async def delete_one(self, id: str):
        async with get_db() as session:
            repo = BancaRepository(session)
            await repo.delete_one(id)
