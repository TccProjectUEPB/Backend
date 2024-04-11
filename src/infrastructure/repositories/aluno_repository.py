from typing import Dict, Any
from src.infrastructure.database.schemas import Aluno
from src.application.models import AlunoModel, AlunoList
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import update, select, delete
from json import loads

class AlunoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any]):
        insert_stmt = Aluno.__table__.insert().returning(
            Aluno.id, Aluno.email, Aluno.created_at, Aluno.updated_at)\
            .values(**data)
        result = (await self.session.execute(insert_stmt)).fetchone()
        if result:
            result = loads(AlunoModel(id=result[0], email=result[1], created_at=result[2], updated_at=result[3])\
                .model_dump_json())
            await self.session.commit()
        return result

    async def get_one(self, id):
        return loads(str(await self.session.get_one(Aluno, id)))

    async def get_all(self):
        stmt = select(Aluno).limit(100)
        stream = await self.session.stream_scalars(stmt.order_by(Aluno.id))
        return loads(AlunoList(root=[aluno async for aluno in stream]).model_dump_json())

    async def update_one(self, id, data):
        update_stmt = Aluno.__table__.update().returning(
            Aluno.id, Aluno.email, Aluno.created_at, Aluno.updated_at)\
            .where(Aluno.id == id)\
            .values(**data)
        result = (await self.session.execute(update_stmt)).fetchone()
        if result:
            result = loads(AlunoModel(id=result[0], email=result[1], created_at=result[2], updated_at=result[3])\
                .model_dump_json())
            await self.session.commit()
        return result
    
    async def delete_one(self, id):
        await self.session.execute(delete(Aluno).where(Aluno.id == id))
        await self.session.commit()
