import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from . import Base
from datetime import datetime


class Auth(Base):
    __tablename__ = "auth"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    matricula = Column(String, unique=True, nullable=False, index=True)
    user_type = Column(String, nullable=False)
    senha = Column(String)
    last_login = Column(DateTime, default=datetime.utcnow)
    foreign_id = Column(String, nullable=False)


    def __repr__(self) -> str:
        return f"Auth(id={self.id!r}, username={self.username!r}, matricula={self.matricula!r}" \
                + f", user_type={self.user_type}, last_login={self.last_login}, foreign_id={self.foreign_id})"
