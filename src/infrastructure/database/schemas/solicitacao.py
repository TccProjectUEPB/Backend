from typing import Optional
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID, TEXT
from sqlalchemy.sql import func

from src.infrastructure.database.schemas import Professor, Aluno
from . import Base


class Solicitacao(Base):
    __tablename__ = "solicitacao"
    __table_args__ = (UniqueConstraint('aluno_id', 'professor_id'),)

    aluno_id = Column(UUID(as_uuid=True), ForeignKey("aluno.id"), primary_key=True)
    professor_id = Column(UUID(as_uuid=True), ForeignKey("professor.id"), primary_key=True)
    status= Column(String(20))
    description = Column(String(150))
    comment = Column(TEXT)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    # association between Assocation -> Child
    professor = relationship(Professor, backref = "professor")

    # association between Assocation -> Parent
    aluno = relationship(Aluno, backref="aluno")

    def __repr__(self) -> str:
        return f"Solicitacao(id={self.id!r}, email={self.email!r})"

