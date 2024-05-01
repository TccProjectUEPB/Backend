from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


from .aluno import Aluno
from .professor import Professor
from .auth import Auth
from .admin import Admin
from .solicitacao import Solicitacao
from .orientacao import Orientacao
from .banca import Banca
from .tarefa import Tarefa
