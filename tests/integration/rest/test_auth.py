import pytest


@pytest.mark.parametrize(
    "data",
    [
        ({"login": "admin", "password": "admin123"}, 200),
        ({"login": "admin", "password": "invalid_password"}, 401),
        ({"login": "invalid_user", "password": "invalid_password"}, 401),
    ],
)
@pytest.mark.asyncio_cooperative
async def test_login_with_valid_input(client, data):
    request, response = await client.post("/v1/auth", json=data[0])
    assert response.status == data[1]
