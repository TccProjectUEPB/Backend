from src.application.domain.models import CreateSolicitacaoModel, SolicitacaoModel, SolicitacaoQueryModel, CreateOrientacaoModel
from src.application.domain.utils import RequestType, OrientationType
from src.infrastructure.database import get_db
from src.infrastructure.repositories import (
    AlunoRepository,
    ProfessorRepository,
    SolicitacaoRepository,
    OrientacaoRepository,
)
from src.presenters.exception import ConflictException, ValidationException
from src.presenters.helpers import HttpRequest


class SolicitacaoService:
    async def get_one(self, id):
        raise NotImplementedError("Not implemented")

    async def get_all(self, request: HttpRequest):
        query = SolicitacaoQueryModel(**request.query).query_dict()
        async with get_db() as session:
            repo = SolicitacaoRepository(session)
            return await repo.get_all(query)

    async def get_all_of_prof(self, id, request: HttpRequest):
        query = SolicitacaoQueryModel(**{**request.query, **{"professor_id": [id]}})\
            .query_dict()
        async with get_db() as session:
            repo = SolicitacaoRepository(session)
            return await repo.get_all(query)

    async def create(self, request: HttpRequest):
        solicitacao = CreateSolicitacaoModel(**request.body)
        solicitacao.status = RequestType.PENDENTE.value
        result = None
        async with get_db() as session:
            repo = SolicitacaoRepository(session)
            aluno_repo = AlunoRepository(session)
            professor_repo = ProfessorRepository(session)
            orientation_repo = OrientacaoRepository(session)
            aluno = await aluno_repo.get_one(solicitacao.aluno_id)
            if not aluno:
                raise ValidationException(
                    "Invalid aluno", "Aluno does not exist")
            prof = await professor_repo.get_one(solicitacao.professor_id)
            if not prof:
                raise ValidationException(
                    "Invalid Professor", "Professor does not exist")
            elif prof["available"]:
                raise ConflictException(
                    "Invalid status", "professor is not available or inconsistent data provided")
            if await repo.get_all({"query": {
                "aluno_id": solicitacao.aluno_id,
                "professor_id": solicitacao.professor_id,
                    "status": RequestType.PENDENTE.value}, "limit": 1}):
                raise ConflictException(
                    "Already exist", "Solicitacao  already exist")
            if not await orientation_repo.has_active(solicitacao.aluno_id, solicitacao.professor_id):
                try:
                    result = await repo.create(
                        solicitacao.model_dump(exclude_none=True, exclude={
                            "id"}),
                        commit=True
                    )
                    return result
                except BaseException as err:
                    print(err)
                    await session.rollback()
                    raise ConflictException(
                        "Unknow Error", "Unknow Error")
            raise ConflictException(
                "Invalid status", "already exists an active orientation")

    async def update_one(self, related_id: str, id: str, request: HttpRequest):
        professor = SolicitacaoModel(**request.body)
        async with get_db() as session:
            repo = SolicitacaoRepository(session)
            try:
                result = await repo.update_one(id, professor.model_dump(
                    exclude_none=True, exclude={"id", "aluno_id", "professor_id", "description", "comment"}), commit=False)
                if result:
                    if result["status"] == RequestType.ACEITO.value:
                        orientation_repo = OrientacaoRepository(session)
                        print(await orientation_repo.get_all({"query": {"solicitacao_id": result["id"]}, "limit": 10}))
                        await orientation_repo.create(CreateOrientacaoModel(
                            aluno_id=result["aluno_id"],
                            professor_id=result["professor_id"]
                        ).model_dump(exclude_none=True))
                    elif result["status"] == RequestType.REJEITADO.value:
                        await session.commit()

            except BaseException:
                await session.rollback()
                raise ConflictException("Already created", "Already created")

    async def delete_one(self, id: str):
        async with get_db() as session:
            repo = SolicitacaoRepository(session)
            await repo.delete_one(id)
