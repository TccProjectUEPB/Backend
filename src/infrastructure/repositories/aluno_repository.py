from typing import Dict, Any
from src.infrastructure.database.schemas import Aluno
from src.application.domain.models import AlunoModel, AlunoList
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import update, select, delete
from json import loads


class AlunoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any], commit = True):
        insert_stmt = Aluno.__table__.insert().returning(
            Aluno.id, Aluno.name, Aluno.email, Aluno.created_at, Aluno.updated_at)\
            .values(**data)
        result = (await self.session.execute(insert_stmt)).fetchone()
        if result:
            result = loads(AlunoModel(id=result[0], name=result[1], email=result[2], created_at=result[3], updated_at=result[4])
                           .model_dump_json())
            commit and await self.session.commit()
        return result

    async def get_one(self, id):
        get_one_stmt = select(Aluno).where(Aluno.id == id).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        if result:
            result = result[0]
            result = loads(AlunoModel(id=result.id, name=result.name, email=result.email, created_at=result.created_at, updated_at=result.updated_at)
                           .model_dump_json())
        return result

    async def get_all(self, filters={}):
        stmt = select(Aluno).filter_by(**filters["query"]).limit(filters["limit"])
        stream = await self.session.stream_scalars(stmt.order_by(Aluno.id))
        return loads(AlunoList(root=[aluno async for aluno in stream]).model_dump_json())

    async def update_one(self, id, data):
        update_stmt = Aluno.__table__.update().returning(
            Aluno.id, Aluno.name, Aluno.email, Aluno.created_at, Aluno.updated_at)\
            .where(Aluno.id == id)\
            .values(**data)
        result = (await self.session.execute(update_stmt)).fetchone()
        if result:
            result = loads(AlunoModel(id=result[0], name=result[1], email=result[2], created_at=result[3], updated_at=result[4])
                           .model_dump_json())
            await self.session.commit()
        return result

    async def delete_one(self, id):
        await self.session.execute(delete(Aluno).where(Aluno.id == id))
        await self.session.commit()
