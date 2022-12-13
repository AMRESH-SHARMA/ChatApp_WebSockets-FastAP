from sqlalchemy import Column, Integer, String
from .database import Base


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
