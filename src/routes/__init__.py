from sanic.blueprints import BlueprintGroup
from .aluno_route import ALUNO

ROUTES = BlueprintGroup(
    ALUNO,
)