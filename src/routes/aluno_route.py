from typing import List
from src.application.models import AlunoModel
from src.infrastructure.database import get_db
from sanic import Blueprint, request, response
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
)

ALUNO = Blueprint("aluno")


@ALUNO.route("/aluno/create", methods=["POST"])
async def create_post(request: request):
    # validation
    aluno = AlunoModel(**request.json)
    # repository interaction
    session: AsyncSession = get_db()
    session.add(aluno)
    await session.commit()
    # await session.refresh(db_post)
    return response.json("")