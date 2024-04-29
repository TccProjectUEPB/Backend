from sanic import Request
from src.application.domain.utils import UserTypes
from src.presenters.helpers import HttpResponse
from http import HTTPStatus


def admin_or_id(field):
    def func(next):
        async def verify(request: Request, *args, **kwargs):
            if request.ctx.user_type == UserTypes.ADMIN.value:
                return await next(request, *args, **kwargs)
            if field not in kwargs:
                return HttpResponse.build(
                    "UNAUTHORIZED", HTTPStatus.UNAUTHORIZED, content_type="plain/text"
                )
            elif kwargs[field] != request.ctx.user_id:
                return HttpResponse.build(
                    "UNAUTHORIZED", HTTPStatus.UNAUTHORIZED, content_type="plain/text"
                )
            return await next(request, *args, **kwargs)

        return verify

    return func