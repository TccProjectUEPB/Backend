from src.application.domain.models import UpdateOrientacaoModel, OrientacaoQueryModel
from src.infrastructure.database import get_db
from src.infrastructure.repositories import (
    OrientacaoRepository,
)
from src.presenters.helpers import HttpRequest


class OrientacaoService:
    async def get_one_by_prof(self, related_id: str, id: str, request: HttpRequest):
        async with get_db() as session:
            repo = OrientacaoRepository(session)
            result = await repo.get_one(id)
            if result and result["professor_id"] == related_id:
                return result
            return None
        
    async def get_one_by_aluno(self, related_id: str, id: str, request: HttpRequest):
        async with get_db() as session:
            repo = OrientacaoRepository(session)
            result = await repo.get_one(id)
            if result and result["aluno_id"] == related_id:
                return result
            return None

    async def get_all(self, request: HttpRequest):
        query = OrientacaoQueryModel(**request.query).query_dict()
        async with get_db() as session:
            repo = OrientacaoRepository(session)
            return await repo.get_all(query)

    async def update_one(self, related_id: str, id: str, request: HttpRequest):
        orientation = UpdateOrientacaoModel(**request.body)
        async with get_db() as session:
            repo = OrientacaoRepository(session)
            return await repo.update_one(related_id, id, orientation.model_dump(
                    exclude_none=True), commit=False)

    async def delete_one(self, id: str):
        async with get_db() as session:
            repo = OrientacaoRepository(session)
            await repo.delete_one(id)
