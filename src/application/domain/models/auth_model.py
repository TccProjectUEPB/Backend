from typing import Optional, List
from pydantic import BaseModel, StrictStr, ConfigDict, Field, field_serializer
from uuid import UUID
from datetime import datetime


class AuthModel(BaseModel):

    id: Optional[UUID] = None
    username: StrictStr
    matricula: StrictStr
    user_type: StrictStr
    password: StrictStr
    refresh_token: Optional[StrictStr] = None
    last_login: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )
    foreign_id: UUID