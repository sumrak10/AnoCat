from ..utils.repository import SQLAlchemyRepository
from ..models.mails import Mails

class MailsRepository(SQLAlchemyRepository):
    model = Mails