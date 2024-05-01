from typing import Optional, List, Union, Dict, Any
from .query_model import QueryModel
from src.application.domain.utils import TarefaType, TypeOpStr, TypeOpDate
from pydantic import (
    BaseModel,
    RootModel,
    ConfigDict,
    Field,
    field_serializer,
    StrictStr,
)
from uuid import UUID
from datetime import datetime


class CreateTarefaModel(BaseModel):
    id: Optional[UUID] = None
    orientation_id: Optional[UUID] = None
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    status: TarefaType = TarefaType.EM_PROGRESSO.value
    deadline: Optional[datetime] = None
    extra: Optional[Dict[str, Any]] = None
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


class TarefaModel(BaseModel):
    id: Optional[UUID] = None
    orientation_id: Optional[UUID] = None
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    status: Optional[TarefaType] = None
    deadline: Optional[datetime] = None
    extra: Optional[Dict[str, Any]] = None
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


class UpdateTarefaModel(BaseModel):
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    status: Optional[TarefaType] = None
    deadline: Optional[datetime] = None
    extra: Optional[Dict[str, Any]] = None
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


class TarefaList(RootModel):
    root: List[TarefaModel]


class TarefaQueryModel(QueryModel):
    id: Optional[List[UUID]] = None
    orientation_id: Optional[List[UUID]] = None
    title: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    description: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    status: Optional[List[Union[TypeOpStr, StrictStr]]] = None
    deadline: Optional[List[Union[TypeOpDate, StrictStr]]] = None

    def integrate_regex(text: str):
        # text = f"^{text}" if text[0] != ["*"] else text.replace("*", ".*", 1)
        # text = f"{text}$" if text[-1] != ["*"] else text.replace("*", ".*", 1)

        return text  # .replace("*", ".*")
