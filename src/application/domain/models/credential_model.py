from pydantic import BaseModel, StrictStr, Field, field_validator
from pydantic_core import PydanticCustomError
import re


class CreateAuthModel(BaseModel):
    username: StrictStr = Field(..., min_length=6)
    matricula: StrictStr = Field(..., min_length=6)
    password: StrictStr = Field(
        ...,
        min_length=6,
        max_length=60,
    )
    @field_validator("password")
    @classmethod
    def v_password(cls, value: str) -> str:
        if re.search(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", value):
            return value
        raise PydanticCustomError("Invalid Password",
            "Minimum eight characters, at least one letter, one number and one special character",
            dict(wrong_value=value),
        )
    @field_validator("matricula")
    @classmethod
    def v_matricula(cls, value: str) -> str:
        if value.isdigit():
            return value
        raise PydanticCustomError("Invalid Matricula",
            "Must be a number",
            dict(wrong_value=value),
        )
        

class CredentialModel(BaseModel):
    login: StrictStr
    password: StrictStr


class RefreshCredentialModel(BaseModel):
    access_token: StrictStr
    refresh_token: StrictStr


class ResetCredentialModel(BaseModel):
    email: StrictStr
    old_password: StrictStr
    new_password: StrictStr
