from enum import Enum


class RequestType(Enum):
    PENDENTE = "pendente",
    REJEITADO = "rejeitado",
    ACEITO = "aceito",
