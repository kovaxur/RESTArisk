from ServeYourself.modules.DB import DB
from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declarative_base
from DB.DB import DB
from settings import Settings

class UserDB(DB):
    Base = declarative_base()

    def __init__(self):
        super().__init__(Settings.getConfigValue("authorization", "user"),
                         Settings.getConfigValue("authorization", "password"),
                         Settings.getConfigValue("authorization", "host"),
                         Settings.getConfigValue("authorization", "db"),
                         Settings.getConfigValue("authorization", "type"))

    def create_db(self):
        self.Base.metadata.create_all(bind=self.engine)

    class Roles(Base):
        __tablename__ = 'roles'

        id = Column(Integer,  primary_key=True, nullable=False)
        name = Column(String(10), nullable=False)