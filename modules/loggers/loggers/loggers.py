import logging


def get_handler(toFile=False, path=None, level=20):

    if not toFile:
        ch = logging.StreamHandler()
    else:
        if path is None:
            raise Exception('If you want to logging to file, say me where!')
        ch = logging.FileHandler(path)
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    return(ch)

def get_logger(handler=None,logger_name='Main_logger', level=20):
    '''
    Level	Numeric value
    CRITICAL	50
    ERROR	40
    WARNING	30
    INFO	20
    DEBUG	10
    NOTSET	0
    '''

    if handler is None:
        raise Exception('Hey! If you want to get a logger, first provide a handler!')

    # create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    # create formatter
    logger.addHandler(handler)
    return(logger)

def set_basic_logging(toFile=False, path=None, level=20):

    if not toFile:
        logging.basicConfig(level=level,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    else:
        if path is None:
            raise Exception('If you want to logging to file, say me where!')
        logging.basicConfig(filename=path,level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



    return(logging)