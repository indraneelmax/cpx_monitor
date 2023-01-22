import os
import sys
import logging

LOG_DEBUG_ENV = "CPX_MONITOR_DEBUG"
FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

LOG_LEVEL = logging.DEBUG if os.getenv(LOG_DEBUG_ENV) else logging.INFO


class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    format = "%(message)s"
    RED_FORMAT = red + format + reset
    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        # log_fmt = self.FORMATS.get(record.levelno)
        if hasattr(record, 'color'):
            log_fmt = self.RED_FORMAT
        else:
            log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_console_handler():
    """
    Returns the console handler.
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(CustomFormatter())
    return console_handler


def get_logger(logger_name):
    """
    Args:
        logger_name (str): Name for the logger

    Retruns:
        logger: A logger 
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(get_console_handler())
    logger.propagate = False
    return logger
