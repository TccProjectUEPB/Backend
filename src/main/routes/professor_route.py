from src.application.models import ProfessorModel
from src.infrastructure.database import get_db
from src.infrastructure.repositories import ProfessorRepository
from sanic import Blueprint, request, response


PROFESSOR = Blueprint("professor")

@PROFESSOR.route("/professores", methods=["POST"])
async def create_professor(request: request):
    professor = ProfessorModel(**request.json)\
        .model_dump(exclude_none=True, exclude={"id"})
    result = None
    async with get_db() as session:
        repo = ProfessorRepository(session)
        result = await repo.create(professor)
    return response.json(result, status=201)

@PROFESSOR.route("/professores", methods=["GET"])
async def get_professores(request: request):
    result = None
    async with get_db() as session:
        repo = ProfessorRepository(session)
        result = await repo.get_all()
    return response.json(result)

@PROFESSOR.route("/professores/<professor_id:str>", methods=["GET"])
async def get_professor(request: request, professor_id: str):
    result = None
    async with get_db() as session:
        repo = ProfessorRepository(session)
        result = await repo.get_one(professor_id)
    return response.json(result)

@PROFESSOR.route("/professores/<professor_id:str>", methods=["PATCH"])
async def update_professor(request: request, professor_id: str):
    professor = ProfessorModel(**request.json)
    result = None
    async with get_db() as session:
        repo = ProfessorRepository(session)
        result = await repo.update_one(professor_id, professor.model_dump(exclude_none=True))
    return response.json(result)

@PROFESSOR.route("/professores/<professor_id:str>", methods=["DELETE"])
async def delete_aluno(request: request, professor_id: str):
    result = None
    async with get_db() as session:
        repo = ProfessorRepository(session)
        result = await repo.delete_one(professor_id)
    return response.json(result)
