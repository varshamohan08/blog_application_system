import logging
from django.conf import settings
from datetime import datetime

class ErrorLogger(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.ERROR)

        logger_handler = logging.FileHandler(str(settings.BASE_DIR)+'/log/error.log')
        logger_handler.setLevel(logging.ERROR)

        logger_formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(lineno)d - %(module)s - %(funcName)s - %(levelname)s - %(message)s - %(details)s')

        logger_handler.setFormatter(logger_formatter)

        self.logger.addHandler(logger_handler)