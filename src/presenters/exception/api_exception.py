from typing import Optional


class ApiException(Exception):
    code: int
    description: str
    redirect_link: str

    def __init__(
        self,
        code: int,
        message: str,
        description: str,
        redirect_link: Optional[str] = None,
    ) -> None:
        super(ApiException, self).__init__(message)
        self.code = code
        self.message = message
        self.description = description

    def to_json(self) -> dict:
        return {
            "code": self.code,
            "message": self.message,
            "description": self.description,
        }