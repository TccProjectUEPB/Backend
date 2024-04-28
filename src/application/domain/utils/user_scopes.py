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
    ]

    GESTOR = [
        "al:ra",
        "al:r",  # Aluno
        "pf:ra",
        "pf:avr",
        "pf:r",
        "pf:u",  # Professor
    ]

    PROFESSOR = [
        "al:ra",
        "al:r",  # Aluno
        "pf:ra",
        "pf:r",
        "pf:u",  # Professor
    ]

    ALUNO = [
        "al:r",  # Aluno
        "al:ra",
        "pf:avr",
        "al:u",
    ]