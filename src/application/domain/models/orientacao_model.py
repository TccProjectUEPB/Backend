from typing import Optional, List, Union
from .query_model import QueryModel
from src.application.domain.utils import OrientationType, TypeOpStr, TypeOpBool
from pydantic import (
    BaseModel, RootModel, ConfigDict,
    Field, field_serializer,
    StrictStr
)
from uuid import UUID
from datetime import datetime


class CreateOrientacaoModel(BaseModel):
    id: Optional[UUID] = None
    aluno_id: UUID
    professor_id: UUID
    status: StrictStr = OrientationType.EM_ANDAMENTO.value
    title: StrictStr = ""
    description: StrictStr = ""
    metodology: StrictStr = ""
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


class OrientacaoModel(BaseModel):
    id: Optional[UUID] = None
    aluno_id: UUID
    professor_id: UUID
    title: StrictStr
    description: StrictStr
    description: StrictStr
    metodology: StrictStr
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


class OrientacaoList(RootModel):
    root: List[OrientacaoModel]


class OrientacaoQueryModel(QueryModel):
    id: Optional[List[UUID]] = None
    professor_id: Optional[List[UUID]] = None
    status: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    title: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    metodology: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    

    def integrate_regex(text: str):
        # text = f"^{text}" if text[0] != ["*"] else text.replace("*", ".*", 1)
        # text = f"{text}$" if text[-1] != ["*"] else text.replace("*", ".*", 1)

        return text  # .replace("*", ".*")
