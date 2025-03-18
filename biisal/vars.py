# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "ʜᴋ ꜱᴛʀᴇᴀᴍ ʙᴏᴛ"
bisal_channel = "https://t.me/TG_BOTS_UPDATE"
bisal_grp = "https://t.me/Hari_Search"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '15671595'))
    API_HASH = str(getenv('API_HASH', 'bb8f36f9c39a24c7f8b2acbc7ea8c60a'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '7697237102:AAFqMGBY66aVK1-sAczjP_5ROpWf8Hd5CWk'))
    name = str(getenv('name', 'HK_Streamx_Bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002210651858'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002170171844'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "7253187871").split()]
    NO_PORT = bool(getenv('NO_PORT', True))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Harikushal'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', 'appropriate-corry-koyebuser123-031b46d3.koyeb.app/') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://anikush8310:AmEPHgfyBCgjGcAF@cluster0.tsu0s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'TG_BOTS_UPDATE')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @Harikushal ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
