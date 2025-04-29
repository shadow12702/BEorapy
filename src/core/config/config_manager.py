# Description: ConfigManager

from admin.data.model.config.app_config_model import AppConfigModel
from admin.data.model.config.jwt_auth_config_model import JwtAuthConfigModel
from admin.data.model.config.mail_config_model import MailConfigModel
from admin.services.config_service import ConfigService
from base.model.mapped_base_model import MappedBaseModel
from helper import helper
from logger import AppLogger
from utils.crypto import Crypto
from core.config.config_loader import cf_loader

class ConfigManager:
    '''Initilizing the configuration for application'''
    _instance = None    
    _logger = AppLogger().get_logger()
    
    def __new__(cls, service: ConfigService = None):
        if not cls._instance:
            if service is None:
                raise ValueError("ConfigService instance must be provided for the first initialization")
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.service = service
            cls._instance._config = {}
            cls._instance._app_config = {}
            cls._instance._jwt_auth = {}
            cls._instance._mail_config = {}            
            cls._instance._update_callback = None
        return cls._instance
    
    async def load_config(self):
        '''Load config from database'''
        self._config = await self.service.all_config()
        self._app_config = await self.service.get_config("application")
        self._jwt_auth = await self.service.get_config("jwt_auth")
        self._mail_config = await self.service.get_config("mail")        
        self._logger.info(f"Config loaded: {self._config}")
        
        if self._update_callback:
            self._update_callback()

    
    async def reload_config(self):
        '''Reload config after update'''
        await self.load_config()

    def set_metadata_update_callback(self, callback):
        """Register a callback function to notify FastAPI when config updates"""
        self._update_callback = callback

    @property
    def all_config(self):
        config = helper.to_nested_dict({k: helper.to_nested_dict(v) if isinstance(v, dict) else v 
                                                for k, v in self._config.items()})
        return MappedBaseModel(**config)
    
    @property
    def app_config(self):
        '''Application config'''
        try:
            _app_config = self._app_config
            defaultAppConfig = AppConfigModel(Title="OraPy", Description="Orapy Assessment Database system", Version="v1.0", MaxThread = 8)
            key_mapping = {
                "description": "Description",
                "title": "Title",
                "language": "Language",
                "version": "Version",
                "max_thread": "MaxThread",
                "awr_default_interval_time": "AwrDefaultIntervalTime",
            }
            mapped = {
                key_mapping[k]: (int(v) if key_mapping[k] == "MaxThread" else v) for k, v in _app_config.items()
            }
            return AppConfigModel(**mapped) if mapped else defaultAppConfig

        except Exception as ex:
            self._logger.error(f"Can't get Application Config: {ex}")
            return defaultAppConfig
        
    @property
    def jwt_auth_config(self):
        'JwtAuth config'
        try:
            def safe_convert(value):
                try:
                    return int(value)
                except (ValueError, TypeError):  
                    return value 

            _jwt_auth = self._jwt_auth
            key_mapping = {
                "jwt_auth_key" : "JwtAuthKey",
                "algorithm" : "Algorithm",
                "token_expire_minutes" :"TokenExpireMinutes",
                "refresh_expire_days" : "RefreshExpireDays"
            }
            mapped = {
                key_mapping[k]: safe_convert(v) for k, v in _jwt_auth.items()
            }
            return JwtAuthConfigModel(**mapped)
        except:
            return JwtAuthConfigModel()
        
    @property
    def mail_config(self):
        'Mail config'
        try:
            _mail = helper.to_nested_dict(self._mail_config)
            _mail["config"]["password"] = Crypto(cf_loader.crypto.Key).decrypt(_mail["config"]["password"])
            key_mapping = {
                "config": { 
                    "sender": "Sender",
                    "password": "Password",
                    "smtp_server": "SmtpServer",
                    "smtp_port": "SmtpPort",
                    "use_ssl": "UseSsl"
                    },
                "body":{
                    "activate": "Activate",
                    "lock_account": "LockAccount"
                }
            }
            target = helper.map_keys(_mail, key_mapping)
            return MailConfigModel(**target)
        except:
            return MailConfigModel()
        