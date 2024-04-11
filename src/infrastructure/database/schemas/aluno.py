import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from . import Base


class Aluno(Base):
    __tablename__ = "aluno"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return '{"id": "' + str(self.id) + '", "email": "' + self.email \
            + '", "created_at": "' + self.created_at +'", "updated_at": "' + self.updated_at+ '"}'

