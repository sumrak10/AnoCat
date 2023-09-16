from abc import ABC, abstractmethod

from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    @abstractmethod
    def get_schema() -> BaseModel:
        raise NotImplementedError