import logging
import os
from logging.handlers import RotatingFileHandler

class LoggerManager:
    @staticmethod
    def setup_logger(log_file='app.log', level=logging.DEBUG):
        logger = logging.getLogger()
        logger.setLevel(level)

        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_path = os.path.join(log_dir, log_file)

        handler = RotatingFileHandler(log_path, maxBytes=5*1024*1024, backupCount=2, encoding='utf-8')
        handler.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(logging.StreamHandler())

        urllib3_logger = logging.getLogger('urllib3')
        urllib3_logger.setLevel(logging.DEBUG)
        urllib3_logger.addHandler(handler)

        return logger
