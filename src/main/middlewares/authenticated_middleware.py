from sanic import Request
from src.presenters.helpers import HttpResponse
from src.utils import settings
from http import HTTPStatus
import jwt


def authenticated(scope):
    def func(next):
        async def auth(request: Request, *args, **kwargs):
            if not request.token:
                return HttpResponse.build(
                    "Authentication failed for lack of authentication credentials.",
                    HTTPStatus.UNAUTHORIZED,
                    content_type="plain/text",
                )
            try:
                payload = jwt.decode(request.token, settings.JWT_SECRET, "HS256", verify=True)
            except BaseException as err:
                return HttpResponse.build(
                    err.args[0],
                    HTTPStatus.UNAUTHORIZED,
                    content_type="plain/text",
                )
            if f"'{scope}'" not in payload["scope"]:
                return HttpResponse.build(
                    "UNAUTHORIZED", HTTPStatus.UNAUTHORIZED, content_type="plain/text"
                )
            request.ctx.user_id = payload["sub"]
            request.ctx.user_type = payload["type"]
            return await next(request, *args, **kwargs)

        return auth

    return func