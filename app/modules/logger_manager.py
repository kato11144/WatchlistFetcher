import logging
import os
from logging.handlers import RotatingFileHandler

class LoggerManager:
    def __init__(self):
        self.level = logging.DEBUG
        self.dir_name = 'logs'
        self.file_name = 'app.log'
        self.file_path = os.path.join(self.dir_name, self.file_name)
        os.makedirs(self.dir_name, exist_ok=True)

    def setup_logger(self):
        logger = logging.getLogger()
        logger.setLevel(self.level)

        handler = RotatingFileHandler(self.file_path, maxBytes=5*1024*1024, backupCount=2, encoding='utf-8')
        handler.setLevel(self.level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(logging.StreamHandler())

        urllib3_logger = logging.getLogger('urllib3')
        urllib3_logger.setLevel(self.level)
        urllib3_logger.addHandler(handler)

        return logger
