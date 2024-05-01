from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, TEXT, JSONB
from sqlalchemy.sql import func

from . import Base


class Tarefa(Base):
    __tablename__ = "tarefa"

    id = Column(UUID(as_uuid=True), primary_key=True)
    orientation_id = Column(UUID(as_uuid=True), ForeignKey("orientacao.id"))
    title = Column(String(60))
    description = Column(TEXT)
    status = Column(String(20))
    deadline = Column(DateTime, nullable=True)
    extra = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return (
            '{"orientation_id":"'
            + str(self.orientation_id)
            + '", "title": "'
            + str(self.title)
            + '", '
            + '", "description": "'
            + str(self.description)
            + '", '
            + '", "status": "'
            + str(self.status)
            + '", '
            + '", "extra": "'
            + str(self.extra)
            + '", '
            + "}"
        )
