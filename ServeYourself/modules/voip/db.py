from DB.DB import DB
from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declarative_base


class Database(DB):
    Base = declarative_base()

    def __init__(self, user: str = None, password: str = None, host: str = None, db: str = None,
                 type: str = 'postgresql'):
        super().__init__(user, password, host, db, type)

    def create_db(self):
        self.Base.metadata.create_all(bind=self.engine)

    class Sipfriends(Base):
        __tablename__ = 'sipfriends'

        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(10), nullable=False)
        ipaddr = Column(String(15), server_default=None)
        port = Column(Integer, server_default=None)
        regseconds = Column(Integer, server_default=None)
        defaultuser = Column(String(10), server_default=None)
        fullcontact = Column(String(35), server_default=None)
        regserver = Column(String(20), server_default=None)
        useragent = Column(String(20), server_default=None)
        lastms = Column(Integer, server_default=None)
        host = Column(String(40), server_default=None)
        type = Column(Enum('friend', 'user', 'peer', name='typeT'), server_default=None)
        context = Column(String(40), server_default=None)
        permit = Column(String(40), server_default=None)
        deny = Column(String(40), server_default=None)
        secret = Column(String(40), server_default=None)
        md5secret = Column(String(40), server_default=None)
        remotesecret = Column(String(40), server_default=None)
        transport = Column(Enum('udp', 'tcp', 'udp,tcp', 'tcp,udp', name='transportT'), server_default=None)
        dtmfmode = Column(Enum('rfc2833', 'info', 'shortinfo', 'inband', 'auto', name='dtmfmodeT'), server_default=None)
        directmedia = Column(Enum('yes', 'no', 'nonat', 'update', name='directmediaT'), server_default=None)
        nat = Column(Enum('yes', 'no', 'never', 'route', name='natT'), server_default=None)
        callgroup = Column(String(40), server_default=None)
        pickupgroup = Column(String(40), server_default=None)
        language = Column(String(40), server_default=None)
        allow = Column(String(40), server_default=None)
        disallow = Column(String(40), server_default=None)
        insecure = Column(String(40), server_default=None)
        trustrpid = Column(Enum('yes', 'no', name='trustrpidT'), server_default=None)
        progressinband = Column(Enum('yes', 'no', 'never', name='progressinbandT'), server_default=None)
        promiscredir = Column(Enum('yes', 'no', name='promiscredirT'), server_default=None)
        useclientcode = Column(Enum('yes', 'no', name='useclientcodeT'), server_default=None)
        accountcode = Column(String(40), server_default=None)
        setvar = Column(String(40), server_default=None)
        callerid = Column(String(40), server_default=None)
        amaflags = Column(String(40), server_default=None)
        callcounter = Column(Enum('yes', 'no', name='callcounterT'), server_default=None)
        busylevel = Column(Integer, server_default=None)
        allowoverlap = Column(Enum('yes', 'no', name='allowoverlapT'), server_default=None)
        allowsubscribe = Column(Enum('yes', 'no', name='allowsubscribeT'), server_default=None)
        videosupport = Column(Enum('yes', 'no', name='videosupportT'), server_default=None)
        maxcallbitrate = Column(Integer, server_default=None)
        rfc2833compensate = Column(Enum('yes', 'no', name='rfc2833compensateT'), server_default=None)
        mailbox = Column(String(40), server_default=None)
        session_timers = Column(Enum('accept', 'refuse', 'originate', name='sessiontimersT'),
                                server_default=None, name='session-timers')
        session_expires = Column(Integer, server_default=None, name='session-expires')
        session_minse = Column(Integer, server_default=None, name='session-minse')
        session_refresher = Column(Enum('uac', 'uas', name='sessionrefresherT'),
                                   server_default=None, name='session-refresher')
        t38pt_usertpsource = Column(String(40), server_default=None, name='t38pt_usertpsource')
        regexten = Column(String(40), server_default=None)
        fromdomain = Column(String(40), server_default=None)
        fromuser = Column(String(40), server_default=None)
        qualify = Column(String(40), server_default=None)
        defaultip = Column(String(40), server_default=None)
        rtptimeout = Column(Integer, server_default=None)
        rtpholdtimeout = Column(Integer, server_default=None)
        sendrpid = Column(Enum('yes', 'no', name='sendrpidT'), server_default=None)
        outboundproxy = Column(String(40), server_default=None)
        callbackextension = Column(String(40), server_default=None)
        registertrying = Column(Enum('yes', 'no', name='registertryingT'), server_default=None)
        timert1 = Column(Integer, server_default=None)
        timerb = Column(Integer, server_default=None)
        qualifyfreq = Column(Integer, server_default=None)
        constantssrc = Column(Enum('yes', 'no', name='constantssrcT'), server_default=None)
        contactpermit = Column(String(40), server_default=None)
        contactdeny = Column(String(40), server_default=None)
        usereqphone = Column(Enum('yes', 'no', name='usereqphoneT'), server_default=None)
        textsupport = Column(Enum('yes', 'no', name='textsupportT'), server_default=None)
        faxdetect = Column(Enum('yes', 'no', name='faxdetectT'), server_default=None)
        buggymwi = Column(Enum('yes', 'no', name='buggymwiT'), server_default=None)
        auth = Column(String(40), server_default=None)
        fullname = Column(String(40), server_default=None)
        trunkname = Column(String(40), server_default=None)
        cid_number = Column(String(40), server_default=None, name='cid_number')
        callingpres = Column(Enum('allowed_not_screened', 'allowed_passed_screen', 'allowed_failed_screen',
                                  'allowed', 'prohibscreened', 'prohib_passed_screen', 'prohib_failed_screen',
                                  'prohib', name='callingpresT'), server_default=None)
        mohintegererpret = Column(String(40), server_default=None)
        mohsuggest = Column(String(40), server_default=None)
        parkinglot = Column(String(40), server_default=None)
        hasvoicemail = Column(Enum('yes', 'no', name='hasvoicemailT'), server_default=None)
        subscribemwi = Column(Enum('yes', 'no', name='subscribemwiT'), server_default=None)
        vmexten = Column(String(40), server_default=None)
        autoframing = Column(Enum('yes', 'no', name='autoframingT'), server_default=None)
        rtpkeepalive = Column(Integer, server_default=None)
        call_limit = Column(Integer, server_default=None, name='call-limit')
        g726nonstandard = Column(Enum('yes', 'no', name='g726nonstandardT'), server_default=None)
        ignoresdpversion = Column(Enum('yes', 'no', name='ignoresdpversionT'), server_default=None)
        allowtransfer = Column(Enum('yes', 'no', name='allowtransferT'), server_default=None)
        dynamic = Column(Enum('yes', 'no', name='dynamicT'), server_default=None)


if __name__ == "__main__":
    from pprint import pprint

    asterisk = Asterisk(type='memory')
    asterisk.create_db()
    session = asterisk.session()
    user = Asterisk.Sipfriends(id=1, name='Joska', ipaddr='1.1.1.1')
    session.add(user)
    user2 = session.query(Asterisk.Sipfriends).filter_by(name='Joska').first()
    pprint(user2)
    print(user is user2)


