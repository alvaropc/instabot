from telegram.ext import Updater
from loggers import loggers
import os

logging=loggers.set_basic_logging()
logging.info('hola')



instatoken = os.environ.get('INSTATOKEN')

updater = Updater(token= os.environ.get('INSTATOKEN'))
dispatcher = updater.dispatcher
