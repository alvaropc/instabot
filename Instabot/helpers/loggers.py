import logging


class Loggers:
    def __init__(self, logger_name = "Main_logger", output_path=None, level = 20):

        ch = self.__get_handler(level, output_path)
        self._logger = self.__get_logger(level, ch, logger_name)

    @staticmethod
    def __get_handler(level, output_path=None):

        if output_path is None:
            ch = logging.StreamHandler()
        else:
            ch = logging.FileHandler(output_path)
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        return ch

    @staticmethod
    def __get_logger(level, handler=None, logger_name='Main_logger'):
        """
          Level	Numeric value
        CRITICAL	50
        ERROR	40
        WARNING	30
        INFO	20
        DEBUG	10
        NOTSET	0
        :param handler:
        :param logger_name:
        :param level:
        :return:
        """

        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value
