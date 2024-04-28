from typing import Dict, Any
from src.infrastructure.database.schemas import Professor
from src.application.domain.models import ProfessorModel, ProfessorList
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import update, select, delete
from json import loads


class ProfessorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any], commit = True):
        insert_stmt = Professor.__table__.insert().returning(
            Professor.id, Professor.name, Professor.email, Professor.available, Professor.created_at, Professor.updated_at)\
            .values(**data)
        result = (await self.session.execute(insert_stmt)).fetchone()
        if result:
            result = loads(ProfessorModel(id=result[0], name=result[1], email=result[2], available=result[3], created_at=result[4], updated_at=result[5])
                           .model_dump_json())
            commit and await self.session.commit()
        return result

    async def get_one(self, id):
        get_one_stmt = select(Professor).where(Professor.id == id).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        if result:
            result = result[0]
            result = loads(ProfessorModel(id=result.id, name=result.name, email=result.email, created_at=result.created_at, updated_at=result.updated_at)
                           .model_dump_json())
        return result

    async def get_all(self, filters={}):
        stmt = select(Professor).filter_by(**filters["query"]).limit(filters["limit"])
        stream = await self.session.stream_scalars(stmt.order_by(Professor.id))
        return loads(ProfessorList(root=[professor async for professor in stream]).model_dump_json())

    async def update_one(self, id, data):
        update_stmt = Professor.__table__.update().returning(
            Professor.id, Professor.name, Professor.email, Professor.available, Professor.created_at, Professor.updated_at)\
            .where(Professor.id == id)\
            .values(**data)
        result = (await self.session.execute(update_stmt)).fetchone()
        if result:
            result = loads(ProfessorModel(id=result[0], name=result[1], email=result[2], available=result[3], created_at=result[4], updated_at=result[5])
                           .model_dump_json())
            await self.session.commit()
        return result

    async def delete_one(self, id):
        await self.session.execute(delete(Professor).where(Professor.id == id))
        await self.session.commit()


    async def check_status(self, id):
        get_status_stmt = select(Professor.status).where(Professor.id == id).limit(1)
        result = await self.session.execute(get_status_stmt)
        status = result.scalar()
        return status

