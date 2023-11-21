from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (Boolean, Column, ForeignKey, Integer, MetaData, String,
                        inspect)
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = MetaData()


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    hashed_password = Column(String(length=320), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)


class Note(Base):
    __tablename__ = "note"
    __metadata__ = metadata

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))

    def to_dict(self):
        column_names = inspect(self.__class__).columns.keys()
        result = {k: self.__dict__[k] for k in column_names}
        return result
