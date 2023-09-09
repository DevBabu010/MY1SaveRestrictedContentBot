#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default="26909410", cast=int)
API_HASH = config("API_HASH", default="e700aa9ee91c332dfecb4ba0b6536dac")
BOT_TOKEN = config("BOT_TOKEN", default="6257702782:AAEpqz6SCB6OvdppyZtqvrush9ry3PuoHCU")
SESSION = config("SESSION", default= "BQGamuIARKZjStB5z7FT28jXotuapbL2YEDOSg0YxUajyZf4Wi4pT-UrhYRWqVnqpl7eEkevYocAsjIfAYzIpScSkkDcQRPnHQkWGjyc6zT2BMBo56IdaH2CtgZgLfNSCWajvOBP18y1JVg8GoXPu20H23AA1AED1_gvPr4lw6r6dVDKpq5ss2JMUooZMQ175z_dT1SlsFfY1lNYDVw917li7Bv_gfGQfunMRJODFRddF2OdRv09ugtxy5hBayckfp4dRrlgQtFx0gOIEaQvhuhoRTJlDAls_Ac5E_Gy9dvHoLgVWJ3BTcOL1gH1_7m_9qem4CnW6nkDldNCphv9aYBE5mgyRgAAAAFXKswHAA")
FORCESUB = config("FORCESUB", default="https://t.me/srcbots")
AUTH = config("AUTH", default="5757389831", cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
