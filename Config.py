mport os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6053350620:AAHtXBr82rsewQ_XRK3JDuhfGUNrNQ3ngrQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzMBu5ru7Oz3ktl2tR-dEYt65tJXgq0STSsHPTSPUGnWQZtjJ6G74hFtQstngflQu_4RtVm5YjH_i2qTlW5_ng6O3CaDMgC8zJvH_QWkIVaMVGtLFbj4foNXd9ZK5D75ExpeylEpAIOlypus1yOuKLRBPrGDmiRHLtD1yzLTMQx_u-HiFLel4_h1dc0_Lu4yUTG6oV6zZMlIi92XJryKbwK7FJ4oiHSD6NGs29sKmmQOJQwQ5QTg8wG7AOaoKTPNSls8lbmDzWqTWVZPfTC2p6nZdnK5ICfdf8dxmYwLnELtENa59YfGsJ873h2mHj6z1Wqa71WmTm1qj87oR5WJEz-6GZE=") #pastw string Sess
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "sawertwzxcsan_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6016219802")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
