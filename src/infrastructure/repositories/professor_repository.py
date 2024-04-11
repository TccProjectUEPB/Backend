from src.infrastructure.database.schemas import Professor
from src.application.models import ProfessorModel, ProfessorList
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import update, select, delete
from json import loads


class ProfessorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, object: Professor):
        self.session.add(object)
        await self.session.commit()

    async def get_one(self, id):
        return loads(str(await self.session.get_one(Professor, id)))

    async def get_all(self):
        stmt = select(Professor).limit(100)
        stream = await self.session.stream_scalars(stmt.order_by(Professor.id))
        return loads(ProfessorList(root=[professor async for professor in stream]).model_dump_json())

    async def update_one(self, id, data):
        update_statement = Professor.__table__.update().returning(
            Professor.id, Professor.email, Professor.created_at, Professor.updated_at)\
            .where(Professor.id == id)\
            .values(**data)
        result = (await self.session.execute(update_statement)).fetchone()
        if result:
            result = loads(ProfessorModel(id=result[0], email=result[1], created_at=result[2], updated_at=result[3])\
                .model_dump_json())
            await self.session.commit()
        return result 
    
    async def delete_one(self, id):
        await self.session.execute(delete(Professor).where(Professor.id == id))
        await self.session.commit()
