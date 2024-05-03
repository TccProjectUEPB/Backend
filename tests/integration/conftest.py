import pytest

# from test_dir.integration.config.collection import ()


@pytest.fixture(scope="session")
async def client():
    """Criando app para teste"""
    from src import app

    return app.asgi_client
