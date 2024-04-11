from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
class Base(AsyncAttrs, DeclarativeBase):
    pass
from .aluno import Aluno
from .professor import Professor
from .solicitacao import Solicitacao
