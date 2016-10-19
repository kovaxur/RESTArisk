from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, Session


class DB():
    def __init__(self, user, password, host, db, type='postgresql'):
        self._user = user
        self._password = password
        self._host = host
        self._db = db
        self._type = type
        self._engine = None
        self._session = None

    def set_engine(self):
        if self._type == 'memory':
            connect_string = 'sqlite:///:memory:'
        else:
            connect_string = self._type + '://' + self._user + ':' + self._password + "@" + self._host + '/' + self._db
        self._engine = create_engine(connect_string)

    def set_session(self):
        if not self._engine:
            self.set_engine()
        self._session = sessionmaker(bind=self.engine)


    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, db):
        self._db = db

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def engine(self):
        if not self._engine:
            self.set_engine()
        return self._engine

    @property
    def session(self):
        if not self._session:
            self.set_session()
        return self._session


if __name__ == "__main__":
    a = DB('a','b','c','d','e')
    print(a, a.user)
