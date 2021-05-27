from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base
from sqlalchemy import create_engine

engine = create_engine('postgresql://dima:secret@localhost:5432/test_db')
conn = engine.connect()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    def to_json(self):
        to_serialize = ['id', 'name', 'value']
        d = {}
        for attr_name in to_serialize:
            d[attr_name] = getattr(self, attr_name)
        return d


Index('my_index', MyModel.name, unique=True, mysql_length=255)
