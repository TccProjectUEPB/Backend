from src.application.domain.utils import UserTypes, UserScopes
from src.infrastructure.database import get_db
from src.infrastructure.repositories import AuthRepository
from src.utils import settings
import bcrypt


class DefaultAdminTask:
    def __init__(self):
        pass

    @classmethod
    async def run(cls):
        async with get_db() as session:
            repo = AuthRepository(session)
            if not await repo.get_one_by_username(settings.ADMIN_USERNAME):
                password = bcrypt.hashpw(
                    settings.ADMIN_PASSWORD.encode(), bcrypt.gensalt(13)
                ).decode()
                result = await repo.create({"username": settings.ADMIN_USERNAME,
                                      "matricula": "000001",
                                      "password": password, "user_type": UserTypes.ADMIN.value})
                print("admin created", result)
                
        #self.logger.info("Successfully created the default admin")