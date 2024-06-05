import pytest


@pytest.mark.parametrize(
    "data",
    [
        (
            {
                "name": "Roger araujo",
                "username": "rogerio",
                "matricula": "000002",
                "password": "Aluno123!",
                "email": "roger@gmail.com",
            },
            401,
        )
    ],
)
@pytest.mark.asyncio_cooperative
async def test_cadastro_with_professor(delete_users, professor_scope, client, data):
    request, response = await client.post(
        "/v1/alunos",
        json=data[0],
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {professor_scope}",
        },
    )
    assert response.status == data[1]


@pytest.mark.parametrize(
    "data",
    [
        (
            {
                "name": "Roger araujo",
                "username": "rogerio",
                "matricula": "000002",
                "password": "Aluno123!",
                "email": "roger@gmail.com",
            },
            401,
        )
    ],
)
@pytest.mark.asyncio_cooperative
async def test_cadastro_with_aluno(delete_users, aluno_scope, client, data):
    request, response = await client.post(
        "/v1/alunos",
        json=data[0],
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {aluno_scope}",
        },
    )
    assert response.status == data[1]


@pytest.mark.parametrize(
    "data",
    [
        (
            {
                "name": "Roger araujo",
                "username": "rogerio",
                "matricula": "000002",
                "password": "Aluno123!",
                "email": "roger@gmail.com",
            },
            201,
        )
    ],
)
@pytest.mark.asyncio_cooperative
async def test_cadastro_with_gestor(delete_users, gestor_scope, client, data):
    request, response = await client.post(
        "/v1/alunos",
        json=data[0],
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {gestor_scope}",
        },
    )
    assert response.status == data[1]


@pytest.mark.parametrize(
    "data",
    [
        (
            {
                "name": "Roger araujo",
                "username": "rogerio",
                "matricula": "000002",
                "password": "Aluno123!",
                "email": "roger@gmail.com",
            },
            201,
        )
    ],
)
@pytest.mark.asyncio_cooperative
async def test_cadastro_with_admin(delete_users, admin_scope, client, data):
    request, response = await client.post(
        "/v1/alunos",
        json=data[0],
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {admin_scope}",
        },
    )
    assert response.status == data[1]


@pytest.mark.parametrize(
    "data",
    [
        (
            {
                "name": "Roger araujo",
                "username": "rogerio",
                "matricula": "000002",
                "password": "Aluno123!",
                "email": "roger@gmail.com",
            },
            201,
        )
    ],
)
@pytest.mark.asyncio_cooperative
async def test_cadastro_with_valid_input(delete_users, admin_scope, client, data):
    request, response = await client.post(
        "/v1/alunos",
        json=data[0],
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {admin_scope}",
        },
    )
    assert response.status == data[1]


@pytest.mark.parametrize(
    "data",
    [
        (
            {},
            400,
        ),
        (
            {
                "username": "roger",
                "matricula": "00001",
                "password": "aluno123",
                "email": "roger@gmail.com",
            },
            400,
        ),
        (
            {
                "name": "Roger araujo",
                "matricula": "00001",
                "password": "aluno123",
                "email": "roger@gmail.com",
            },
            400,
        ),
        (
            {
                "name": "Roger araujo",
                "username": "roger",
                "password": "aluno123",
                "email": "roger@gmail.com",
            },
            400,
        ),
        (
            {
                "name": "Roger araujo",
                "username": "roger",
                "matricula": "00001",
                "email": "roger@gmail.com",
            },
            400,
        ),
        (
            {
                "name": "Roger araujo",
                "username": "roger",
                "matricula": "00001",
                "password": "aluno123",
            },
            400,
        ),
    ],
)
@pytest.mark.asyncio_cooperative
async def test_cadastro_with_invalid_input(delete_users, admin_scope, client, data):
    request, response = await client.post(
        "/v1/alunos",
        json=data[0],
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {admin_scope}",
        },
    )
    assert response.status == data[1]
