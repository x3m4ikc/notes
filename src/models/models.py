from datetime import datetime
from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP, ForeignKey, inspect
from db.database import Base

metadata = MetaData()


class User(Base):
    __tablename__ = "users"
    __metadata__ = metadata

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def to_dict(self):
        column_names = inspect(self.__class__).columns.keys()
        result = {k: self.__dict__[k] for k in column_names}
        return result

class Note(Base):
    __tablename__ = "notes"
    __metadata__ = metadata

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
