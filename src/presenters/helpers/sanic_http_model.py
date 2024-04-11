from typing import Dict

from sanic import response

# from bson.json_util import dumps
from json import dumps


class HttpRequest:
    @classmethod
    def build(
        cls,
        header: Dict = None,
        body: Dict = None,
        query: Dict = None,
        extra: Dict = None,
    ):
        cls.header = header
        cls.body = body
        cls.query = query
        cls.extra = extra

        return HttpRequest


class HttpResponse:
    @staticmethod
    def build(
        body: any = None,
        status_code: int = 200,
        headers={},
        content_type="application/json",
    ):
        if content_type == "application/json":
            body = dumps(body)
        return response.text(
            body,
            status=status_code,
            content_type=content_type,
            headers=headers,
        )