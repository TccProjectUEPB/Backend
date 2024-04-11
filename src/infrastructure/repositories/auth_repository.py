from typing import Dict, Any
from src.infrastructure.database.schemas import Auth
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import update, select, delete
from json import loads


class AuthRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any], commit = True):
        insert_stmt = Auth.__table__.insert().returning(
            Auth.id, Auth.matricula, Auth.username, Auth.foreign_id, Auth.user_type, Auth.last_login)\
            .values(**data)
        result = (await self.session.execute(insert_stmt)).fetchone()
        if result:
            commit and await self.session.commit()
        return result

    async def get_one(self, id):
        get_one_stmt = select(Auth).where(Auth.id == id).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        return result

    async def get_one_by_username(self, username):
        get_one_stmt = select(Auth).where(Auth.username == username).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        return result

    async def get_one_by_matricula(self, matricula):
        get_one_stmt = select(Auth).where(Auth.matricula == matricula).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        return result

    async def get_all(self):
        stmt = select(Auth).limit(100)
        stream = await self.session.stream_scalars(stmt.order_by(Auth.id))
        return [aluno async for aluno in stream]

    async def update_one(self, id, data):
        update_stmt = Auth.__table__.update().returning(
            Auth.id, Auth.username, Auth.matricula, Auth.last_login, Auth.user_type)\
            .where(Auth.id == id)\
            .values(**data)
        result = (await self.session.execute(update_stmt)).fetchone()
        if result:
            await self.session.commit()
        return result
    
    async def delete_one(self, id):
        await self.session.execute(delete(Auth).where(Auth.id == id))
        await self.session.commit()
