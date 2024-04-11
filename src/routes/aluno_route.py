from typing import List
from src.application.models import AlunoModel
from src.infrastructure.database import get_db
from src.infrastructure.database.schemas import Aluno
from src.infrastructure.repositories import AlunoRepository
from sanic import Blueprint, request, response
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
)


ALUNO = Blueprint("aluno")

@ALUNO.route("/alunos", methods=["POST"])
async def create_aluno(request: request):
    aluno = AlunoModel(**request.json)\
        .model_dump(exclude_none=True, exclude={"id"})
    result = None
    async with get_db() as session:
        repo = AlunoRepository(session)
        result = await repo.create(aluno)
    return response.json(result, status=201)

@ALUNO.route("/alunos", methods=["GET"])
async def get_alunos(request: request):
    result = None
    async with get_db() as session:
        repo = AlunoRepository(session)
        result = await repo.get_all()
    return response.json(result)

@ALUNO.route("/alunos/<aluno_id:str>", methods=["GET"])
async def get_aluno(request: request, aluno_id: str):
    result = None
    async with get_db() as session:
        repo = AlunoRepository(session)
        result = await repo.get_one(aluno_id)
    return response.json(result)

@ALUNO.route("/alunos/<aluno_id:str>", methods=["PATCH"])
async def update_aluno(request: request, aluno_id: str):
    aluno = AlunoModel(**request.json)
    result = None
    async with get_db() as session:
        repo = AlunoRepository(session)
        result = await repo.update_one(aluno_id, aluno.model_dump(exclude_none=True))
    return response.json(result)

@ALUNO.route("/alunos/<aluno_id:str>", methods=["DELETE"])
async def delete_aluno(request: request, aluno_id: str):
    result = None
    async with get_db() as session:
        repo = AlunoRepository(session)
        result = await repo.delete_one(aluno_id)
    return response.json(result)
