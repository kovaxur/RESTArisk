from voip.db import Database
from settings import Settings
from flask import session


class AsteriskSIP:

    def __init__(self):
        self.database = Database(Settings.getConfigValue("voip", "user"),
                                 Settings.getConfigValue("voip", "password"),
                                 Settings.getConfigValue("voip", "host"),
                                 Settings.getConfigValue("voip", "db"),
                                 Settings.getConfigValue("voip", "type"),
                                 )

    def get_sip_peers(self):
        db_session = self.database.session()
        # TODO: need to modify name = to ownchacc= later, need to change the schame too!
        sipfriends = db_session.query(self.database.Sipfriends).filter_by(name=session['schacc']).first()
        return sipfriends.name

