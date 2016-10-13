CREATE TYPE typeT AS ENUM ('friend','user','peer');
CREATE TYPE transportT as ENUM ('udp','tcp','udp,tcp','tcp,udp');
CREATE TYPE dtmfmodeT as ENUM ('rfc2833','info','shortinfo','inband','auto');
CREATE TYPE directmediaT as ENUM ('yes','no','nonat','update');
CREATE TYPE natT as ENUM ('yes','no','never','route');
CREATE TYPE trustrpidT as ENUM ('yes','no');
CREATE TYPE progressinbandT as ENUM ('yes','no','never');
CREATE TYPE promiscredirT as ENUM ('yes','no');
CREATE TYPE useclientcodeT as ENUM ('yes','no');
CREATE TYPE callcounterT as ENUM ('yes','no');
CREATE TYPE allowoverlapT as ENUM ('yes','no');
CREATE TYPE allowsubscribeT as ENUM ('yes','no');
CREATE TYPE videosupportT as ENUM ('yes','no');
CREATE TYPE rfc2833compensateT as ENUM ('yes','no');
CREATE TYPE sessiontimersT as ENUM ('accept','refuse','originate');
CREATE TYPE sessionrefresherT as ENUM ('uac','uas');
CREATE TYPE sendrpidT as ENUM('yes','no');
CREATE TYPE registertryingT as ENUM('yes','no');
CREATE TYPE constantssrcT as ENUM('yes','no');
CREATE TYPE usereqphoneT as ENUM('yes','no');
CREATE TYPE textsupportT as ENUM('yes','no');
CREATE TYPE faxdetectT as ENUM('yes','no');
CREATE TYPE buggymwiT as ENUM('yes','no');
CREATE TYPE callingpresT as ENUM('allowed_not_screened','allowed_passed_screen','allowed_failed_screen','allowed','prohibscreened','prohib_passed_screen','prohib_failed_screen','prohib');
CREATE TYPE hasvoicemailT as ENUM('yes','no');
CREATE TYPE subscribemwiT as ENUM('yes','no');
CREATE TYPE autoframingT as ENUM('yes','no');
CREATE TYPE g726nonstandardT as ENUM('yes','no');
CREATE TYPE ignoresdpversionT as ENUM('yes','no');
CREATE TYPE allowtransferT as ENUM('yes','no');
CREATE TYPE dynamicT as ENUM('yes','no');


CREATE TABLE IF NOT EXISTS sipfriends (
      id INTEGER NOT NULL,
      name varchar(10) NOT NULL,
      ipaddr varchar(15) DEFAULT NULL,
      port INTEGER DEFAULT NULL,
      regseconds INTEGER DEFAULT NULL,
      defaultuser varchar(10) DEFAULT NULL,
      fullcontact varchar(35) DEFAULT NULL,
      regserver varchar(20) DEFAULT NULL,
      useragent varchar(20) DEFAULT NULL,
      lastms INTEGER DEFAULT NULL,
      host varchar(40) DEFAULT NULL,
      type typeT DEFAULT NULL,
      context varchar(40) DEFAULT NULL,
      permit varchar(40) DEFAULT NULL,
      deny varchar(40) DEFAULT NULL,
      secret varchar(40) DEFAULT NULL,
      md5secret varchar(40) DEFAULT NULL,
      remotesecret varchar(40) DEFAULT NULL,
      transport transportT DEFAULT NULL,
      dtmfmode dtmfmodeT DEFAULT NULL,
      directmedia directmediaT DEFAULT NULL,
      nat natT DEFAULT NULL,
      callgroup varchar(40) DEFAULT NULL,
      pickupgroup varchar(40) DEFAULT NULL,
      language varchar(40) DEFAULT NULL,
      allow varchar(40) DEFAULT NULL,
      disallow varchar(40) DEFAULT NULL,
      insecure varchar(40) DEFAULT NULL,
      trustrpid trustrpidT DEFAULT NULL,
      progressinband progressinbandT DEFAULT NULL,
      promiscredir promiscredirT DEFAULT NULL,
      useclientcode useclientcodeT DEFAULT NULL,
      accountcode varchar(40) DEFAULT NULL,
      setvar varchar(40) DEFAULT NULL,
      callerid varchar(40) DEFAULT NULL,
      amaflags varchar(40) DEFAULT NULL,
      callcounter callcounterT DEFAULT NULL,
      busylevel INTEGER DEFAULT NULL,
      allowoverlap allowoverlapT DEFAULT NULL,
      allowsubscribe allowsubscribeT DEFAULT NULL,
      videosupport videosupportT DEFAULT NULL,
      maxcallbitrate INTEGER DEFAULT NULL,
      rfc2833compensate rfc2833compensateT DEFAULT NULL,
      mailbox varchar(40) DEFAULT NULL,
      "session-timers" sessiontimersT DEFAULT NULL,
      "session-expires" INTEGER DEFAULT NULL,
      "session-minse" INTEGER DEFAULT NULL,
      "session-refresher" sessionrefresherT DEFAULT NULL,
      t38pt_usertpsource varchar(40) DEFAULT NULL,
      regexten varchar(40) DEFAULT NULL,
      fromdomain varchar(40) DEFAULT NULL,
      fromuser varchar(40) DEFAULT NULL,
      qualify varchar(40) DEFAULT NULL,
      defaultip varchar(40) DEFAULT NULL,
      rtptimeout INTEGER DEFAULT NULL,
      rtpholdtimeout INTEGER DEFAULT NULL,
      sendrpid sendrpidT DEFAULT NULL,
      outboundproxy varchar(40) DEFAULT NULL,
      callbackextension varchar(40) DEFAULT NULL,
      registertrying registertryingT DEFAULT NULL,
      timert1 INTEGER DEFAULT NULL,
      timerb INTEGER DEFAULT NULL,
      qualifyfreq INTEGER DEFAULT NULL,
      constantssrc constantssrcT DEFAULT NULL,
      contactpermit varchar(40) DEFAULT NULL,
      contactdeny varchar(40) DEFAULT NULL,
      usereqphone usereqphoneT DEFAULT NULL,
      textsupport textsupportT DEFAULT NULL,
      faxdetect faxdetectT DEFAULT NULL,
      buggymwi buggymwiT DEFAULT NULL,
      auth varchar(40) DEFAULT NULL,
      fullname varchar(40) DEFAULT NULL,
      trunkname varchar(40) DEFAULT NULL,
      cid_number varchar(40) DEFAULT NULL,
      callingpres callingpresT DEFAULT NULL,
      mohintegererpret varchar(40) DEFAULT NULL,
      mohsuggest varchar(40) DEFAULT NULL,
      parkinglot varchar(40) DEFAULT NULL,
      hasvoicemail hasvoicemailT DEFAULT NULL,
      subscribemwi subscribemwiT DEFAULT NULL,
      vmexten varchar(40) DEFAULT NULL,
      autoframing autoframingT DEFAULT NULL,
      rtpkeepalive INTEGER DEFAULT NULL,
      "call-limit" INTEGER DEFAULT NULL,
      g726nonstandard g726nonstandardT DEFAULT NULL,
      ignoresdpversion ignoresdpversionT DEFAULT NULL,
      allowtransfer allowtransferT DEFAULT NULL,
      dynamic dynamicT DEFAULT NULL
)