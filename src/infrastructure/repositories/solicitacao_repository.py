from typing import Dict, Any
from src.infrastructure.database.schemas import Solicitacao
from src.application.domain.models import SolicitacaoModel, SolicitacaoList
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import update, select, delete
from json import loads


class SolicitacaoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any], commit=True):
        insert_stmt = Solicitacao.__table__.insert().returning(
            Solicitacao.id, Solicitacao.aluno_id, Solicitacao.professor_id, Solicitacao.status,
            Solicitacao.description, Solicitacao.comment, Solicitacao.created_at, Solicitacao.updated_at)\
            .values(**data)
        result = (await self.session.execute(insert_stmt)).fetchone()
        if result:
            result = loads(SolicitacaoModel(
                id=result[0], aluno_id=result[1], professor_id=result[2],
                status=result[3], description=result[4], comment=result[5],
                created_at=result[6], updated_at=result[7])
                .model_dump_json())
            commit and await self.session.commit()
        return result

    async def get_one(self, id):
        get_one_stmt = select(Solicitacao).where(Solicitacao.id == id).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        if result:
            result = result[0]
            result = loads(SolicitacaoModel(
                id=result.id, aluno_id=result.aluno_id, professor_id=result.professor_id,
                status=result.status, description=result.description, comment=result.comment,
                created_at=result.created_at, updated_at=result.updated_at)
                .model_dump_json())
        return result

    async def get_all(self, filters={}):
        stmt = select(Solicitacao).filter_by(
            **filters["query"]).limit(filters["limit"])
        stream = await self.session.stream_scalars(stmt.order_by(Solicitacao.id))
        return loads(SolicitacaoList(root=[solicitacao async for solicitacao in stream]).model_dump_json())

    async def update_one(self, related_id, id, data, commit=True):
        update_stmt = Solicitacao.__table__.update().returning(
            Solicitacao.id, Solicitacao.aluno_id, Solicitacao.professor_id, Solicitacao.status,
            Solicitacao.description, Solicitacao.comment, Solicitacao.created_at, Solicitacao.updated_at)\
            .where(Solicitacao.id == id, Solicitacao.professor_id == related_id)\
            .values(**data)
        result = (await self.session.execute(update_stmt)).fetchone()
        if result:
            result = loads(SolicitacaoModel(
                id=result[0], aluno_id=result[1], professor_id=result[2],
                status=result[3], description=result[4], comment=result[5],
                created_at=result[6], updated_at=result[7])
                .model_dump_json())
            commit and await self.session.commit()
        return result

    async def delete_one(self, id):
        await self.session.execute(delete(Solicitacao).where(Solicitacao.id == id))
        await self.session.commit()

    async def check_status(self, id):
        get_status_stmt = select(Solicitacao.status).where(
            Solicitacao.id == id).limit(1)
        result = await self.session.execute(get_status_stmt)
        status = result.scalar()
        return status
