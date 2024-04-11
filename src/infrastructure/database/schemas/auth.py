import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from . import Base
from datetime import datetime


class Auth(Base):
    __tablename__ = "auth"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String(30), unique=True, nullable=False, index=True)
    matricula = Column(String(40), unique=True, nullable=False, index=True)
    user_type = Column(String(30), nullable=False)
    password = Column(String)
    refresh_token = Column(String, nullable=True)
    last_login = Column(DateTime, nullable=True)
    foreign_id = Column(UUID, nullable=False)


    def __repr__(self) -> str:
        return f"Auth(id={self.id!r}, username={self.username!r}, matricula={self.matricula!r}" \
                + f", user_type={self.user_type}, last_login={self.last_login}, foreign_id={self.foreign_id})"
