import datetime
import logging
import os

from config import DIRECTORY, APP_NAME

directory = DIRECTORY
category = APP_NAME


class MyLogger:
    """
    Class For Handling Logging
    """

    def __init__(self):
        try:

            # Path
            self.category = category
            self.str_date = str(datetime.date.today()).replace('-', '_')
            file_path = os.path.join(directory, self.str_date + '.txt')
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Logging Attributes
            self.logger = logging.getLogger(category)
            if not self.logger.hasHandlers():
                formatter = logging.Formatter('%(asctime)s,%(msecs)d | %(name)s | %(levelname)s | %(message)s')
                handler = logging.FileHandler(file_path, mode='a')
                handler.setFormatter(formatter)
                self.logger.setLevel(logging.INFO)
                self.logger.addHandler(handler)
                # self.logger.propagate = False
            print('Logging Successful')

        except Exception:
            print('Logging Failure')
            raise

    def error_logger(self, error, meta=''):
        # self.logger = logging.getLogger(self.category)
        self.logger.error('-' * 100)
        self.logger.error(error)
        if meta:
            self.logger.error(meta)
