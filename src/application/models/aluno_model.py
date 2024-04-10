from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class AlunoModel(BaseModel):
    id: Optional[UUID]
    name: str
    email: str
    senha: str

    class Config:
        from_attributes = True
