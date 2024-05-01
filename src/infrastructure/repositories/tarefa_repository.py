from typing import Dict, Any
from src.infrastructure.database.schemas import Tarefa
from src.application.domain.models import TarefaModel, TarefaList
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import select, delete
from json import loads


class TarefaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any], commit=True):
        insert_stmt = (
            Tarefa.__table__.insert()
            .returning(
                Tarefa.id,
                Tarefa.orientation_id,
                Tarefa.title,
                Tarefa.description,
                Tarefa.status,
                Tarefa.deadline,
                Tarefa.extra,
                Tarefa.created_at,
                Tarefa.updated_at,
            )
            .values(**data)
        )
        result = (await self.session.execute(insert_stmt)).fetchone()
        if result:
            result = loads(
                TarefaModel(
                    id=result[0],
                    orientation_id=result[1],
                    title=result[2],
                    description=result[3],
                    status=result[4],
                    deadline=result[5],
                    extra=result[6],
                    created_at=result[7],
                    updated_at=result[8],
                ).model_dump_json()
            )
            commit and await self.session.commit()
        return result

    async def get_one(self, id):
        get_one_stmt = select(Tarefa).where(Tarefa.id == id).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        if result:
            result = result[0]
            result = loads(
                TarefaModel(
                    id=result.id,
                    orientation_id=result.orientation_id,
                    title=result.title,
                    description=result.description,
                    status=result.status,
                    deadline=result.deadline,
                    extra=result.extra,
                    created_at=result.created_at,
                    updated_at=result.updated_at,
                ).model_dump_json()
            )
        return result

    async def get_all(self, filters={}):
        stmt = select(Tarefa).filter_by(**filters["query"]).limit(filters["limit"])
        stream = await self.session.stream_scalars(stmt.order_by(Tarefa.id))
        return loads(
            TarefaList(root=[tarefa async for tarefa in stream]).model_dump_json()
        )

    async def update_one(self, id, data):
        update_stmt = (
            Tarefa.__table__.update()
            .returning(
                Tarefa.id,
                Tarefa.orientation_id,
                Tarefa.title,
                Tarefa.description,
                Tarefa.status,
                Tarefa.deadline,
                Tarefa.extra,
                Tarefa.created_at,
                Tarefa.updated_at,
            )
            .where(Tarefa.id == id)
            .values(**data)
        )
        result = (await self.session.execute(update_stmt)).fetchone()
        if result:
            result = loads(
                TarefaModel(
                    id=result[0],
                    orientation_id=result[1],
                    title=result[2],
                    description=result[3],
                    status=result[4],
                    deadline=result[5],
                    extra=result[6],
                    created_at=result[7],
                    updated_at=result[8],
                ).model_dump_json()
            )
            await self.session.commit()
        return result

    async def delete_one(self, id):
        await self.session.execute(delete(Tarefa).where(Tarefa.id == id))
        await self.session.commit()
