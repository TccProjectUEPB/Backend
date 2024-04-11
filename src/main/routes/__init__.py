from sanic import Blueprint
from .aluno_route import ALUNO
from .professor_route import PROFESSOR
from .auth_route import AUTH_ROUTES

ROUTES = Blueprint.group(
    ALUNO,
    PROFESSOR,
    AUTH_ROUTES,
)
