from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, ARRAY, FLOAT
from sqlalchemy.sql import func

from . import Base


class Banca(Base):
    __tablename__ = "banca"

    id = Column(UUID(as_uuid=True), ForeignKey("orientacao.id"), primary_key=True)
    realized_at = Column(DateTime, nullable=True)
    score = Column(FLOAT(2), nullable=True)
    status = Column(String(30))
    analyzers = Column(ARRAY(String(50)))
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
