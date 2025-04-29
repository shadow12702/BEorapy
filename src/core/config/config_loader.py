# Description: 

import configparser
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from admin.data.model.config.db_context_config_model import DbContextConfigModel
from admin.data.model.config.crypto_config_model import CryptoConfigModel
from admin.data.model.config.logging_config_model import LoggingConfigModel
from core.config.config_change_handler import ConfigChangeHandler
from core.config.config_writer import ConfigWriter
from core.enum.app_enum import AppEnum
from utils.crypto import Crypto


CONFIG_CRYPTO_TYPE = "crypto"
CONFIG_CRYPTO_KEY = "secret_key"
CONFIG_DB_CONTEXT_TYPE = "db_context"
CONFIG_LOGGING_TYPE = 'logging'

    
class ConfigLoader:
    '''Initializing to load config from file'''
    _instance = None
        
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._load_config()
            cls._instance._setup_hot_reload()
        return cls._instance
        
    def _load_config(self):
        '''Load from INI file'''
        config = configparser.ConfigParser(interpolation=None)
        config.read(AppEnum.APP_CONFIG_FILE.file_path, encoding='utf-8')
        self.crypto = self._load_crypto(config[CONFIG_CRYPTO_TYPE])
        self.db_context = self._load_db_context(config[CONFIG_DB_CONTEXT_TYPE])
        self.logging = self._load_logging(config[CONFIG_LOGGING_TYPE])
        
    def _load_db_context(self, section: configparser.SectionProxy):
        'Load db_context info'
        crypto = Crypto(self.crypto.Key)
        db_context = DbContextConfigModel(
            MinPoolSize = int(section.get('min_pool_size', 2)),
            MaxPoolSize = int(section.get('max_pool_size', 10)),
            Increment = int(section.get('increment', 1)),
            Username = crypto.decrypt(section.get("username", None)),
            Password = crypto.decrypt(section.get("password", None)),
            Dsn = crypto.decrypt(section.get("dsn", None)),
        )
        return db_context
        
    def _load_crypto(self, section: configparser.SectionProxy):
        'Load cryto info'
        crypto_key = section.get(CONFIG_CRYPTO_KEY, '')
        return CryptoConfigModel(Key = crypto_key)
    
    def _load_logging(self, section: configparser.SectionProxy):
        'Load logging config'
        logging = LoggingConfigModel(
            Level = section.get("level", "INFO").upper(),
            Directory = section.get("directory", "app/logs"),
            FileSuffix = section.get('filename_suffix', 'app'),
            DateFormat = section.get('date_format', '%Y-%m-%d %H:%M:%S'),
            LogFormat = section.get('log_format','%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(funcName)s - %(message)s', 
                                   raw=True),
            )
        return logging
    
    def _crypto_key_validation(self, key) -> str:
        try:            
            Crypto(key)
            return key
        except:
            return self._generate_crypto_key()
        
    def _generate_crypto_key(self):
        secret = Crypto.generate_key()
        ConfigWriter.write(CONFIG_CRYPTO_TYPE, CONFIG_CRYPTO_KEY = secret)
        return secret
    
    def _setup_hot_reload(self):
        '''Set up hot-reload when configuration has been changed'''
        event_handler = ConfigChangeHandler(self, AppEnum.APP_CONFIG_FILE.file_path)
        observer = Observer()
        observer.schedule(event_handler, 
                          path=os.path.dirname(AppEnum.APP_CONFIG_FILE.file_path),
                          recursive=False)


cf_loader = ConfigLoader()