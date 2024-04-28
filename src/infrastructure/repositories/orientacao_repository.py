from typing import Dict, Any
from src.infrastructure.database.schemas import Orientacao
from src.application.domain.models import OrientacaoModel, OrientacaoList
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import update, select, delete
from json import loads


class OrientacaoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any], commit = True):
        insert_stmt = Orientacao.__table__.insert().returning(
            Orientacao.id, Orientacao.name, Orientacao.email, Orientacao.created_at, Orientacao.updated_at)\
            .values(**data)
        result = (await self.session.execute(insert_stmt)).fetchone()
        if result:
            result = loads(OrientacaoModel(id=result[0], name=result[1], email=result[2], created_at=result[3], updated_at=result[4])
                           .model_dump_json())
            commit and await self.session.commit()
        return result

    async def get_one(self, id):
        get_one_stmt = select(Orientacao).where(Orientacao.id == id).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        if result:
            result = result[0]
            result = loads(OrientacaoModel(id=result.id, name=result.name, email=result.email, created_at=result.created_at, updated_at=result.updated_at)
                           .model_dump_json())
        return result

    async def get_all(self, filters={}):
        stmt = select(Orientacao).filter_by(**filters["query"]).limit(filters["limit"])
        stream = await self.session.stream_scalars(stmt.order_by(Orientacao.id))
        return loads(OrientacaoList(root=[aluno async for aluno in stream]).model_dump_json())

    async def update_one(self, id, data):
        update_stmt = Orientacao.__table__.update().returning(
            Orientacao.id, Orientacao.name, Orientacao.email, Orientacao.created_at, Orientacao.updated_at)\
            .where(Orientacao.id == id)\
            .values(**data)
        result = (await self.session.execute(update_stmt)).fetchone()
        if result:
            result = loads(OrientacaoModel(id=result[0], name=result[1], email=result[2], created_at=result[3], updated_at=result[4])
                           .model_dump_json())
            await self.session.commit()
        return result

    async def delete_one(self, id):
        await self.session.execute(delete(Orientacao).where(Orientacao.id == id))
        await self.session.commit()


    async def check_status(self, id):
        get_status_stmt = select(Orientacao.status).where(Orientacao.id == id).limit(1)
        result = await self.session.execute(get_status_stmt)
        status = result.scalar()
        return status
