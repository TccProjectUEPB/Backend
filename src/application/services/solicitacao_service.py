from src.application.domain.models import CreateSolicitacaoModel, SolicitacaoModel, SolicitacaoQueryModel
from src.application.domain.utils import RequestType
from src.infrastructure.database import get_db
from src.infrastructure.repositories import SolicitacaoRepository, AlunoRepository, ProfessorRepository
from src.presenters.exception import ConflictException
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
        print(query)
        async with get_db() as session:
            repo = SolicitacaoRepository(session)
            return await repo.get_all({})

    async def create(self, request: HttpRequest):
        solicitacao = CreateSolicitacaoModel(**request.body)
        solicitacao.status = RequestType.PENDENTE.value
        result = None
        async with get_db() as session:
            repo = SolicitacaoRepository(session)
            aluno_repo = AlunoRepository(session)
            professor_repo = ProfessorRepository(session)
            aluno = await aluno_repo.get_one(solicitacao.aluno_id)
            prof = await professor_repo.get_one(solicitacao.professor_id)
            if aluno and prof and prof["available"]:
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
            else:
                raise ConflictException(
                    "Invalid status", "professor is not available or inconsistent data provided")

    async def update_one(self, id: str, request: HttpRequest):
        professor = SolicitacaoModel(**request.body)
        async with get_db() as session:
            repo = SolicitacaoRepository(session)
            return await repo.update_one(id, professor.model_dump(exclude_none=True))

    async def delete_one(self, id: str):
        async with get_db() as session:
            repo = SolicitacaoRepository(session)
            await repo.delete_one(id)
