from typing import Dict, Any
from src.infrastructure.database.schemas import Admin
from src.application.domain.models import AdminModel, AdminList
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import select, delete
from json import loads


class AdminRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any], commit = True):
        insert_stmt = Admin.__table__.insert().returning(
            Admin.id, Admin.name, Admin.email, Admin.created_at, Admin.updated_at)\
            .values(**data)
        result = (await self.session.execute(insert_stmt)).fetchone()
        if result:
            result = loads(AdminModel(id=result[0], name=result[1], email=result[2], created_at=result[3], updated_at=result[4])
                           .model_dump_json())
            commit and await self.session.commit()
        return result

    async def get_one(self, id):
        get_one_stmt = select(Admin).where(Admin.id == id).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        if result:
            result = result[0]
            result = loads(AdminModel(id=result.id, name=result.name, email=result.email, created_at=result.created_at, updated_at=result.updated_at)
                           .model_dump_json())
        return result

    async def get_all(self, filters={}):
        stmt = select(Admin).filter_by(**filters["query"]).limit(filters["limit"])
        stream = await self.session.stream_scalars(stmt.order_by(Admin.id))
        return loads(AdminList(root=[aluno async for aluno in stream]).model_dump_json())

    async def update_one(self, id, data):
        update_stmt = Admin.__table__.update().returning(
            Admin.id, Admin.name, Admin.email, Admin.created_at, Admin.updated_at)\
            .where(Admin.id == id)\
            .values(**data)
        result = (await self.session.execute(update_stmt)).fetchone()
        if result:
            result = loads(AdminModel(id=result[0], name=result[1], email=result[2], created_at=result[3], updated_at=result[4])
                           .model_dump_json())
            await self.session.commit()
        return result

    async def delete_one(self, id):
        await self.session.execute(delete(Admin).where(Admin.id == id))
        await self.session.commit()
