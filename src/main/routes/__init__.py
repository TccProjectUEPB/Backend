from sanic import Blueprint
from .aluno_route import ALUNO
from .professor_route import PROFESSOR
from .auth_route import AUTH_ROUTES
from .solicitacao_route import SOLICITACAO_ROUTES
from .orientacao_route import ORIENTACAO_ROUTES

ROUTES = Blueprint.group(
    ALUNO,
    PROFESSOR,
    AUTH_ROUTES,
    SOLICITACAO_ROUTES,
    ORIENTACAO_ROUTES,
)
