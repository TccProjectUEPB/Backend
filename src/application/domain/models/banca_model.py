from typing import Optional, List, Union
from .query_model import QueryModel
from src.application.domain.utils import BancaType, TypeOpStr
from pydantic import (
    BaseModel,
    RootModel,
    ConfigDict,
    Field,
    field_serializer,
    StrictStr,
    StrictFloat,
)
from uuid import UUID
from datetime import datetime


class CreateBancaModel(BaseModel):
    id: Optional[UUID] = None
    realized_at: Optional[StrictStr] = None
    score: Optional[StrictFloat] = None
    status: StrictStr = Field(
        BancaType.PENDENTE.value, pattern=BancaType.PENDENTE.value
    )
    analyzers: Optional[List[StrictStr]] = []
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
        json_encoders={
            datetime: lambda dt: dt.replace(microsecond=0).isoformat() + "Z"
        },
    )


class BancaModel(BaseModel):
    id: Optional[UUID] = None
    realized_at: Optional[datetime]
    score: Optional[StrictFloat] = None
    status: Optional[StrictStr] = None
    analyzers: Optional[List[StrictStr]] = None
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
        json_encoders={
            datetime: lambda dt: dt.replace(microsecond=0).isoformat() + "Z"
        },
    )

    @field_serializer("id")
    def serialize_id(self, id):
        return str(id)


class ScheduleBancaModel(BaseModel):
    id: Optional[UUID] = None
    realized_at: datetime
    status: StrictStr = Field(
        BancaType.AGENDADO.value, pattern=BancaType.AGENDADO.value
    )
    analyzers: List[StrictStr] = Field(..., min_length=1, max_length=5)
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True,
        json_encoders={
            datetime: lambda dt: dt.replace(microsecond=0).isoformat() + "Z"
        },
    )


class FinishBancaModel(BaseModel):
    id: Optional[UUID] = None
    status: StrictStr = Field(
        BancaType.FINALIZADO.value, pattern=BancaType.FINALIZADO.value
    )
    score: StrictFloat
    analyzers: List[StrictStr] = Field(min_length=1, max_length=5)
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        from_attributes=True,
        json_encoders={
            datetime: lambda dt: dt.replace(microsecond=0).isoformat() + "Z"
        },
    )


class BancaList(RootModel):
    root: List[BancaModel]


class BancaQueryModel(QueryModel):
    id: Optional[List[UUID]] = None
    professor_id: Optional[List[UUID]] = None
    status: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    title: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    description: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    metodology: Optional[List[Union[TypeOpStr, StrictStr]]] = None

    def integrate_regex(text: str):
        # text = f"^{text}" if text[0] != ["*"] else text.replace("*", ".*", 1)
        # text = f"{text}$" if text[-1] != ["*"] else text.replace("*", ".*", 1)

        return text  # .replace("*", ".*")
