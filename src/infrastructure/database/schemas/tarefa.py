from typing import Optional
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID, TEXT, JSONB
from sqlalchemy.sql import func

from src.infrastructure.database.schemas import Professor, Aluno
from . import Base


class Tarefa(Base):
    __tablename__ = "tarefa"

    orientation_id = Column(UUID(as_uuid=True), ForeignKey(
        "orientacao.id"), primary_key=True)
    title = Column(String(60))
    description = Column(TEXT)
    status = Column(String(20))
    extra = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return '{"orientation_id":"' + str(self.orientation_id) + '", "title": "'+str(self.title)+'", '\
            + '", "description": "'+str(self.description)+'", '+'", "status": "'+str(self.status)+'", '\
            +'", "extra": "'+str(self.extra)+'", '+'}'
