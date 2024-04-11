from typing import Optional, List
from pydantic import BaseModel, RootModel, ConfigDict, Field, field_serializer
from uuid import UUID
from datetime import datetime


class ProfessorModel(BaseModel):
    id: Optional[UUID] = Field(None, alias="id_1")
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
        from_attributes = True,
        json_encoders = {datetime: lambda dt: dt.replace(microsecond=0).isoformat()+"Z"})

    @field_serializer('id')
    def serialize_id(self, id):
        return str(id)

class ProfessorList(RootModel):
    root: List[ProfessorModel]