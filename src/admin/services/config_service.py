# Description: ConfigService

import asyncio
from typing import List
from admin.data.entities.config import Config
from helper import helper
from core.config.config_writer import ConfigWriter
from core.config.config_loader import cf_loader
from logger import AppLogger
from admin.factory import AdminFactory
from utils.crypto import Crypto
from admin.models.response_model import ConfigResponse
from admin.models.request_model import ConfigRequest

class ConfigService:

    _logger = AppLogger().get_logger()

    def __init__(self, admin_factory: AdminFactory):
        self.repository = admin_factory.config_repository()

    async def all_config(self):
        '''Load all config'''
        try:
            all_config = await self.repository.get_all()                        
            return self._format_dict(all_config)
        except Exception as ex:
            self._logger.error(f"load all_config error: {ex}")
            raise ex
    
    async def get_all_config(self):
        try:
            all_config = await self.repository.get_all()            
            return  [
                ConfigResponse(**item.to_response())
                for item in all_config
            ]
        except Exception as ex:
            self._logger.error(f"get_all_config error: {ex}")
            raise ex
        
    async def get_config(self, type: str):
        '''Get App config'''
        _config = await self.repository.get_config_by_type(type)
        result = self._format_dict(_config)
        return result.get(type, {})

    async def write_app(self, **kwargs):
        '''Changing configuration for application section'''
        self._logger.debug("Beginning write app configuration")
        type = "application"
        app_config = await self.get_config(type)
        
        update_tasks = [self.repository.update(type, key, value) for key, value in kwargs.items() if key in app_config]
        write_tasks = [self.repository.write(type, key, value) for key, value in kwargs.items() if key not in app_config]

        # Run update and write tasks concurrently
        await asyncio.gather(*update_tasks, *write_tasks)
    
    async def write_jwt_auth(self, **kwargs):
        '''Changing configuration for JwtAuth section'''
        self._logger.info("Beginning write JwtAuth configuration")
        type = "jwt_auth"
        jwt_config = await self.get_config(type)
    
        update_tasks = [self.repository.update(type, key, value) for key, value in kwargs.items() if key in jwt_config]
        write_tasks = [self.repository.write(type, key, value) for key, value in kwargs.items() if key not in jwt_config]

        # Run update and write tasks concurrently
        await asyncio.gather(*update_tasks, *write_tasks)        
        
    async def write_email(self, **kwargs):
        '''Changing configuration for email'''
        self._logger.info("Beginning to write email config")
        try:
            type = "mail"
            crypto = Crypto(cf_loader.crypto.Key)
            mail_config = await self.get_config(type)         
            mail_request = helper.flatten_dict(kwargs)
        
            update_tasks = [self.repository.update(type, key, crypto.encrypt(value) if key =="config.password" else value) for key, value in mail_request.items() if key in mail_config]
            write_tasks = [self.repository.write(type, key, crypto.encrypt(value) if key =="config.password" else value)  for key, value in mail_request.items() if key not in mail_config]

            # Run update and write tasks concurrently
            await asyncio.gather(*update_tasks, *write_tasks)

        except Exception as ex:
            self._logger.error(f"Writing mail config failed: {ex}")
        
    async def write_db_context(self, **kwargs):
        '''Changing configuration for DbContext section'''
        self._logger.debug("Beginning write DbContext")
        def sync_write_db():
            try:
                type = "db_context"
                crypto = Crypto(cf_loader.crypto.Key)
                updated_kwargs = kwargs.copy()
                updated_kwargs['username'] = crypto.encrypt(updated_kwargs["username"])
                updated_kwargs['password'] = crypto.encrypt(updated_kwargs["password"])
                updated_kwargs['dsn'] = crypto.encrypt(updated_kwargs["dsn"])
                
                ConfigWriter.write(section=type, **updated_kwargs)
                self._logger.debug("DbContext updated..")
            except Exception as ex:
                self._logger.error(f"Write db_context failed: {ex}")
        await asyncio.to_thread(sync_write_db)

    async def write_logging(self, **kwargs):
        '''Changing configuration for Logging section'''
        self._logger.info("Beginning write logging configuration")
        def sync_write_log():                
            try:
                section = "logging"        
                ConfigWriter.write(section=section, **kwargs)
                self._logger.info("Logging updated...")
            except Exception as ex:
                self._logger.error(f"Write log failed {ex}")
        await asyncio.to_thread(sync_write_log)

    def _format_dict(self, config:List[Config]):
        _cf = {}
        for cf in config:
            _cf.setdefault(cf.type, {})[cf.key] = cf.value
        return _cf
   
