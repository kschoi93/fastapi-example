from starlette.testclient import TestClient

from core.database import settings


def get_superuser_token_headers(client: TestClient) -> dict[str, str]:
    login_data = {
        "username": settings.SUPER_USER_NAME,
        "password": settings.SUPER_USER_PASSWORD,
    }
    response = client.post(f"{settings.API_STR}/auth/token", data=login_data)
    tokens = response.json()
    access_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    return headers