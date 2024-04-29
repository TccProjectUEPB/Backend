from enum import Enum


class UserScopes(Enum):
    ADMIN = [
        "ad:c",  # Admin
        "ad:ra",
        "ad:r",
        "ad:u",
        "al:c",  # Aluno
        "al:ra",
        "al:r",
        "al:u",
        "al:d",
        "pf:c",  # Professor
        "pf:ra",
        "pf:avr",
        "pf:r",
        "pf:u",
        "pf:d",
        "slp:r",  # Solicitacao
        "sla:r",
        "sl:c",
        "sl:u",
    ]

    GESTOR = [
        "al:ra",
        "al:r",  # Aluno
        "pf:ra",
        "pf:avr",
        "pf:r",
        "pf:u",  # Professor
        "slp:r",  # Solicitacao
    ]

    PROFESSOR = [
        "al:ra",
        "al:r",  # Aluno
        "pf:ra",
        "pf:r",
        "pf:u",  # Professor
        "slp:r",  # Solicitacao
        "sl:u",
    ]

    ALUNO = [
        "al:r",  # Aluno
        "al:ra",
        "pf:avr",
        "al:u",
        "sl:c",  # Solicitacao
        "sla:r",
    ]