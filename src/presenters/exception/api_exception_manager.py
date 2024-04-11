from .api_exception import ApiException
from .unauthorized_exception import UnauthorizedException
#from .unprocessable_exception import UnprocessableException
from .validation_exception import ValidationException
from pydantic import ValidationError
from http import HTTPStatus
from sanic.exceptions import InvalidUsage
from sqlalchemy.exc import DatabaseError, IntegrityError, StatementError


class ApiExceptionManager:
    @classmethod
    def build(cls, err: Exception) -> ApiException:
        if isinstance(err, ValidationException):
            return ApiException(
                HTTPStatus.BAD_REQUEST.value, err.message, err.description
            )

        if isinstance(err, ValidationError):
            error = err.errors()
            return ApiException(
                HTTPStatus.BAD_REQUEST.value, str(error[0]["msg"]), str(err)
            )

        if isinstance(err, InvalidUsage):
            return ApiException(
                HTTPStatus.BAD_REQUEST.value,
                HTTPStatus.BAD_REQUEST.phrase,
                HTTPStatus.BAD_REQUEST.description,
            )

        if isinstance(err, UnauthorizedException):
            return ApiException(
                HTTPStatus.UNAUTHORIZED.value, err.message, err.description
            )

        if isinstance(err, IntegrityError):
            return ApiException(
                HTTPStatus.CONFLICT.value,
                HTTPStatus.CONFLICT.phrase,
                HTTPStatus.CONFLICT.description,
            )

        if isinstance(err, StatementError):
            return ApiException(
                HTTPStatus.BAD_REQUEST.value,
                HTTPStatus.BAD_REQUEST.phrase,
                err.args[0],
            )

        if isinstance(err, DatabaseError):
            return ApiException(
                HTTPStatus.UNPROCESSABLE_ENTITY.value, err.message, err.description
            )

        # logger.exception("Api: Internal Server Error")
        return ApiException(
            HTTPStatus.INTERNAL_SERVER_ERROR.value,
            HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
            HTTPStatus.INTERNAL_SERVER_ERROR.description,
        )