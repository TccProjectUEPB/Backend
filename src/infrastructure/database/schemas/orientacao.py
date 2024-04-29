import uuid
from typing import Optional
from sqlalchemy import Column, ForeignKey, String, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, TEXT, ARRAY
from sqlalchemy.sql import func

from src.infrastructure.database.schemas import Professor, Aluno
from . import Base


class Orientacao(Base):
    __tablename__ = "orientacao"

    id = Column(UUID(as_uuid=True), ForeignKey(
        "solicitacao.id"), primary_key=True, default=uuid.uuid4, index=True)
    aluno_id = Column(UUID(as_uuid=True), ForeignKey(
        "aluno.id"))
    professor_id = Column(UUID(as_uuid=True), ForeignKey(
        "professor.id"))
    status = Column(String(20), index=True)
    title = Column(String(100))
    description = Column(TEXT)
    metodology = Column(String(40))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    # association between Assocation -> Child
    professor = relationship(Professor, backref="orientacao")

    # association between Assocation -> Parent
    aluno = relationship(Aluno, backref="orientacao")

    def __repr__(self) -> str:
        return '{"aluno_id":"' + str(self.aluno_id) + '", "professor_id": "'+str(self.professor_id)+'", '\
            + '", "status": "'+self.status+'", '+'", "description": "'+self.description+'", '\
            + '", "comment": "'+self.comment+'", '+'}'
