from ..utils.repository import SQLAlchemyRepository
from ..models.topic_of_day import TopicOfDay

class TopicOfDayRepository(SQLAlchemyRepository):
    model = TopicOfDay