from ..utils.repository import SQLAlchemyRepository
from ..models.answers import Answers

class AnswersRepository(SQLAlchemyRepository):
    model = Answers