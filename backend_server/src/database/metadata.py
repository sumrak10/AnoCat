from typing import Any
from abc import ABC, abstractmethod

from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.types import JSON

class Base(DeclarativeBase):
    type_annotation_map = {
        dict[str, Any]: JSON
    }
    @abstractmethod
    def get_schema(self) -> BaseModel:
        raise NotImplementedError