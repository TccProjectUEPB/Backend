from enum import Enum


class RequestType(Enum):
    PENDENTE = "pendente",
    EM_ANDAMENTO = "em_andamento",
    EM_BANCA = "em_banca",
    FINALIZADO = "finalizado",
