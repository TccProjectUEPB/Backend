from enum import Enum


class TarefaType(str, Enum):
    EM_PROGRESSO = "em_progresso"
    EM_REVISAO = "em_revisao"
    FINALIZADA = "finalizada"
