from ..utils.repository import SQLAlchemyRepository
from ..models.topics import Topics

class TopicsRepository(SQLAlchemyRepository):
    model = Topics