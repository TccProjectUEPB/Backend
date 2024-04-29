from typing import Optional, List, Union
from .query_model import QueryModel
from src.application.domain.utils import OrientationType, TypeOpStr
from pydantic import (
    BaseModel, RootModel, ConfigDict,
    Field, field_serializer,
    StrictStr
)
from uuid import UUID
from datetime import datetime


class CreateOrientacaoModel(BaseModel):
    solicitacao_id: Optional[UUID] = None
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

    @field_serializer('solicitacao_id')
    def serialize_id(self, id):
        return str(id)


class OrientacaoModel(BaseModel):
    solicitacao_id: Optional[UUID] = None
    aluno_id: UUID
    professor_id: UUID
    status: StrictStr
    title: StrictStr
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

    @field_serializer('solicitacao_id')
    def serialize_id(self, id):
        return str(id)


class UpdateOrientacaoModel(BaseModel):
    status: Optional[StrictStr] = Field(None,
        pattern=r"{value1}|{value2}".format(value1=OrientationType.EM_BANCA.value,
                                            value2=OrientationType.FINALIZADO.value)
    )
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    metodology: Optional[StrictStr] = None
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True,
        json_encoders={datetime: lambda dt: dt.replace(microsecond=0).isoformat()+"Z"})


class OrientacaoList(RootModel):
    root: List[OrientacaoModel]


class OrientacaoQueryModel(QueryModel):
    solicitacao_id: Optional[List[UUID]] = None
    professor_id: Optional[List[UUID]] = None
    status: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    title: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    description: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    metodology: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    

    def integrate_regex(text: str):
        # text = f"^{text}" if text[0] != ["*"] else text.replace("*", ".*", 1)
        # text = f"{text}$" if text[-1] != ["*"] else text.replace("*", ".*", 1)

        return text  # .replace("*", ".*")
