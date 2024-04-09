import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from src.infrastructure.database.connection import Base, engine


class Aluno(Base):
    __tablename__ = "aluno"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String)
    matricula = Column(String, unique=True, nullable=False, index=True)
    senha = Column(String)

    def __repr__(self) -> str:
        return f"Aluno(id={self.id!r}, email={self.email!r}, matricula={self.matricula!r})"

Base.metadata.create_all(engine)