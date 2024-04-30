from typing import Dict, Any
from src.infrastructure.database.schemas import Banca
from src.application.domain.models import BancaModel, BancaList
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy import select, delete
from json import loads


class BancaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: Dict[str, Any], commit=True):
        insert_stmt = (
            Banca.__table__.insert()
            .returning(
                Banca.id,
                Banca.realized_at,
                Banca.score,
                Banca.status,
                Banca.analyzers,
                Banca.created_at,
                Banca.updated_at,
            )
            .values(**data)
        )
        result = (await self.session.execute(insert_stmt)).fetchone()
        if result:
            result = loads(
                BancaModel(
                    id=result[0],
                    realized_at=result[1],
                    score=result[2],
                    status=result[3],
                    analyzers=result[4],
                    created_at=result[5],
                    updated_at=result[6],
                ).model_dump_json()
            )
            commit and await self.session.commit()
        return result

    async def get_one(self, id):
        get_one_stmt = select(Banca).where(Banca.id == id).limit(1)
        result = (await self.session.execute(get_one_stmt)).fetchone()
        if result:
            result = result[0]
            result = loads(
                BancaModel(
                    id=result.id,
                    realized_at=result.realized_at,
                    score=result.score,
                    status=result.status,
                    analyzers=result.analyzers,
                    created_at=result.created_at,
                    updated_at=result.updated_at,
                ).model_dump_json()
            )
        return result

    async def get_all(self, filters={}):
        stmt = select(Banca).filter_by(**filters["query"]).limit(filters["limit"])
        stream = await self.session.stream_scalars(stmt.order_by(Banca.id))
        return loads(
            BancaList(root=[banca async for banca in stream]).model_dump_json()
        )

    async def update_one(self, id, data):
        update_stmt = (
            Banca.__table__.update()
            .returning(
                Banca.id,
                Banca.realized_at,
                Banca.score,
                Banca.status,
                Banca.analyzers,
                Banca.created_at,
                Banca.updated_at,
            )
            .where(Banca.id == id)
            .values(**data)
        )
        result = (await self.session.execute(update_stmt)).fetchone()
        if result:
            result = loads(
                BancaModel(
                    id=result[0],
                    realized_at=result[1],
                    score=result[2],
                    status=result[3],
                    analyzers=result[3],
                    created_at=result[4],
                    updated_at=result[5],
                ).model_dump_json()
            )
            await self.session.commit()
        return result

    async def delete_one(self, id):
        await self.session.execute(delete(Banca).where(Banca.id == id))
        await self.session.commit()
