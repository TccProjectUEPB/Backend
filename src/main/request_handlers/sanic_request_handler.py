from src.presenters.exception import ApiExceptionManager
from src.presenters.helpers import HttpRequest, HttpResponse
from sanic import Request


async def sanic_request_handler(api_route, request: Request) -> any:
    """Adapter pattern to Sanic
    :param - Sanic Http Request
    :api_route: Composite Routes
    """
    try:
        request = HttpRequest.build(
            header=request.headers,
            body=request.json or {},
            query=request.args,
            extra=request.ctx or {},
        )
        return await api_route(request=request)
    except Exception as err:
        handler_error = ApiExceptionManager.build(err)
        # logger.info(f"{err}: {request.body}")
        return HttpResponse.build(
            handler_error.to_json(), status_code=handler_error.code
        )