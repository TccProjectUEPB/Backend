import uuid
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.dialects.postgresql import UUID

from src.infrastructure.database.connection import Base, engine


class Professor(Base):
    __tablename__ = "professor"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True)
    created_at = Column(DATETIME, default=datetime.now, onupdate=datetime.now)
    updated_at = Column(DATETIME, default=datetime.now, onupdate=datetime.now)

    def __repr__(self) -> str:
        return f"Professor(id={self.id!r}, email={self.email!r})"


Base.metadata.create_all(engine)