from telegram.ext import Updater
from loggers import loggers
logging=loggers.set_basic_logging()
logging.info('hola')


updater = Updater(token='619007291:AAHHj7HVZEKpVROuNUcACIJmS61iYwEYiGs')
dispatcher = updater.dispatcher