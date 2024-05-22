import pytest
from src.infrastructure.database.connection import engine, Base
from src.application.domain.utils import UserTypes, UserScopes
from src.utils import settings, default
from datetime import datetime, timedelta
from uuid import uuid4
import jwt

# from test_dir.integration.config.collection import ()


@pytest.fixture(scope="session")
async def client():
    """Criando app para teste"""
    from src import app

    return app.asgi_client


@pytest.fixture()
async def delete_users():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def getScopeByUserType(self, type: str):
    try:
        UserTypes(type)
        return UserScopes[type.upper()].value
    except ValueError:
        raise Exception("event not listed in events")


@pytest.fixture(scope="session")
async def aluno_scope():
    current = datetime.utcnow()
    user_type = UserTypes.ALUNO
    jwt.encode(
        {
            "sub": str(uuid4()),
            "iss": settings.ISSUER,
            "type": UserTypes.ALUNO,
            "iat": current,
            "scope": str(getScopeByUserType(user_type)),
            "exp": current + timedelta(seconds=default.TOKEN_EXP_TIME),
        },
        settings.JWT_SECRET,
    )


@pytest.fixture(scope="session")
async def professor_scope():
    current = datetime.utcnow()
    user_type = UserTypes.PROFESSOR
    jwt.encode(
        {
            "sub": str(uuid4()),
            "iss": settings.ISSUER,
            "type": UserTypes.PROFESSOR,
            "iat": current,
            "scope": str(getScopeByUserType(user_type)),
            "exp": current + timedelta(seconds=default.TOKEN_EXP_TIME),
        },
        settings.JWT_SECRET,
    )


@pytest.fixture(scope="session")
async def gestor_scope():
    current = datetime.utcnow()
    user_type = UserTypes.GESTOR
    jwt.encode(
        {
            "sub": str(uuid4()),
            "iss": settings.ISSUER,
            "type": UserTypes.GESTOR,
            "iat": current,
            "scope": str(getScopeByUserType(user_type)),
            "exp": current + timedelta(seconds=default.TOKEN_EXP_TIME),
        },
        settings.JWT_SECRET,
    )
