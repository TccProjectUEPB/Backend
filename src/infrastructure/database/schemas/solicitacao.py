from typing import Optional
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID, TEXT

from infrastructure.database.schemas import Professor, Aluno
from src.infrastructure.database.connection import Base, engine


class Solicitacao(Base):
    __tablename__ = "solicitacao"

    aluno_id = Column(UUID(as_uuid=True), ForeignKey("aluno.id"), primary_key=True)
    professor_id = Column(UUID(as_uuid=True), ForeignKey("professor.id"), primary_key=True)
    status= Column(String(20))
    description = Column(String(150))
    comment = Column(TEXT(500))
    created_at = Column(DATETIME, default=datetime.now, onupdate=datetime.now) 
    updated_at = Column(DATETIME, default=datetime.now, onupdate=datetime.now) 

    # association between Assocation -> Child
    professor: Mapped["Professor"] = relationship(back_populates="professor")

    # association between Assocation -> Parent
    aluno: Mapped["Aluno"] = relationship(back_populates="aluno")

    def __repr__(self) -> str:
        return f"Solicitacao(id={self.id!r}, email={self.email!r})"


Base.metadata.create_all(engine)