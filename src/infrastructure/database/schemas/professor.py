import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from src.infrastructure.database.connection import Base, engine


class Professor(Base):
    __tablename__ = "professor"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True)

    def __repr__(self) -> str:
        return f"Professor(id={self.id!r}, email={self.email!r})"


Base.metadata.create_all(engine)