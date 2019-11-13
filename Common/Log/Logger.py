import logging
import sys
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "quant_log.log"

CONSOLE_LEVEL = logging.DEBUG
FILE_LEVEL = logging.DEBUG

class Logger:

    @classmethod
    def __get_console_handler(cls):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        console_handler.setLevel(CONSOLE_LEVEL)
        return console_handler

    @classmethod
    def __get_file_handler(cls):
        file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
        file_handler.setFormatter(FORMATTER)
        file_handler.setLevel(FILE_LEVEL)

        return file_handler

    @classmethod
    def get_logger(cls, logger_name):
        # logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
        logger.addHandler(cls.__get_console_handler())
        logger.addHandler(cls.__get_file_handler())
        # with this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = False
        return logger
