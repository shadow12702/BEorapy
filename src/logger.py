"""Logging method to keep log information"""
import os
import threading
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from core.config.config_loader import cf_loader

LOG_INFO = cf_loader.logging

# create directory folder when not exist
os.makedirs(LOG_INFO.Directory, exist_ok=True)

class AppLogger:
    '''Application logs manager'''
    
    _logger: logging.Logger
    _instance = None
    _lock   = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(AppLogger, cls).__new__(cls, *args, **kwargs)
                    cls._instance._logger = cls._create_logger()
        return cls._instance
    
    @staticmethod
    def _create_logger():
        logger = logging.getLogger(__class__.__name__)
        logger.setLevel(LOG_INFO.Level)
        formatter = logging.Formatter(LOG_INFO.LogFormat)
        formatter.default_time_format = LOG_INFO.DateFormat
        formatter.default_msec_format = "%s.%03d"
        # setting show log to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # setting for writing to file
        filename = f"{datetime.now().strftime('%Y%m%d')}-{LOG_INFO.FileSuffix}.log"
        log_path = os.path.join(LOG_INFO.Directory, filename)
        file_handler = RotatingFileHandler(log_path, maxBytes=10**6, backupCount=5)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        return logger
    
    def get_logger(self):
        '''get logger from instance'''
        return self._logger
    
logger = AppLogger().get_logger()
