from sanic import Blueprint
from .aluno_route import ALUNO
from .professor_route import PROFESSOR

ROUTES = Blueprint.group(
    ALUNO,
    PROFESSOR,
)