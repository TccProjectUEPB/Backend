import pytest


@pytest.mark.parametrize(
    "data",
    [
        (
            {
                "name": "Roger araujo",
                "username": "roger",
                "matricula": "00001",
                "password": "aluno123",
                "email": "roger@gmail.com",
            },
            201,
        ),
    ],
)
@pytest.mark.asyncio_cooperative
async def test_cadastro_with_valid_input(delete_users, client, data):
    request, response = await client.post("/v1/alunos", json=data[0])
    assert response.status == data[1]
