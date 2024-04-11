from typing import Optional, List, Union
from .credential_model import CreateAuthModel
from .query_model import QueryModel
from src.application.domain.utils import TypeOpStr
from pydantic import (
    BaseModel, RootModel, ConfigDict,
    Field, field_serializer,
    EmailStr, StrictStr
)
from uuid import UUID
from datetime import datetime


class CreateProfessorModel(CreateAuthModel):
    id: Optional[UUID] = None
    name: StrictStr = Field(..., min_length=10, max_length=60)
    email: EmailStr = Field(..., min_length=10, max_length=250)
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True,
        json_encoders={datetime: lambda dt: dt.replace(microsecond=0).isoformat()+"Z"})

    @field_serializer('id')
    def serialize_id(self, id):
        return str(id)


class ProfessorModel(BaseModel):
    id: Optional[UUID] = None
    name: Optional[StrictStr] = None
    email: str
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True,
        json_encoders={datetime: lambda dt: dt.replace(microsecond=0).isoformat()+"Z"})

    @field_serializer('id')
    def serialize_id(self, id):
        return str(id)


class ProfessorList(RootModel):
    root: List[ProfessorModel]

class ProfessorQueryModel(QueryModel):
    id: Optional[List[UUID]] = None
    name: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    email: Optional[List[Union[TypeOpStr, StrictStr]]] = None

    def integrate_regex(text: str):
        #text = f"^{text}" if text[0] != ["*"] else text.replace("*", ".*", 1)
        #text = f"{text}$" if text[-1] != ["*"] else text.replace("*", ".*", 1)

        return text#.replace("*", ".*")