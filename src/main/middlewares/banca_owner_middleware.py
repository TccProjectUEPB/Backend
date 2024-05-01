from sanic import Request
from src.application.domain.utils import UserTypes
from src.infrastructure.database.connection import get_db
from src.infrastructure.repositories import OrientacaoRepository
from src.presenters.helpers import HttpResponse
from http import HTTPStatus


def banca_owner(field):
    def func(next):
        async def verify(request: Request, *args, **kwargs):
            if request.ctx.user_type in [UserTypes.ADMIN.value, UserTypes.GESTOR.value]:
                return await next(request, *args, **kwargs)
            if request.ctx.user_id not in kwargs:
                return HttpResponse.build(
                    "UNAUTHORIZED", HTTPStatus.UNAUTHORIZED, content_type="plain/text"
                )
            async with get_db() as session:
                repo = OrientacaoRepository(session)
                result = await repo.get_all(
                    {
                        "query:": {
                            "id": kwargs[field],
                            "professor_id": request.ctx.user_id,
                        },
                        "limit": 1,
                    }
                )
                if not result:
                    return HttpResponse.build(
                        "UNAUTHORIZED",
                        HTTPStatus.UNAUTHORIZED,
                        content_type="plain/text",
                    )
                if result[0]["professor_id"] != request.ctx.user_id:
                    return HttpResponse.build(
                        "UNAUTHORIZED",
                        HTTPStatus.UNAUTHORIZED,
                        content_type="plain/text",
                    )
            return await next(request, *args, **kwargs)

        return verify

    return func
