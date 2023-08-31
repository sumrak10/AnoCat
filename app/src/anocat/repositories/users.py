from ..utils.repository import SQLAlchemyRepository
from ..models.users import Users
from ..schemas.users import UserSchema

class UsersRepository(SQLAlchemyRepository):
    model = Users