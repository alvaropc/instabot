from telegram.ext import Updater
from Instabot.helpers import Loggers, DB

import os

logging = Loggers().logger

instatoken = DB().instabot_token
print(instatoken)
updater = Updater(token=instatoken)
dispatcher = updater.dispatcher
