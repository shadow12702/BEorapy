from fastapi import HTTPException
from admin.services.config_service import ConfigService
from admin.models.request_model import AppConfigRequest, JwtAuthConfigRequest, DbContextConfigRequest, LoggingConfigRequest, MailConfigRequest
from admin.data.entities.config import Config
from admin.models.request_model import ConfigRequest

class ConfigController:
    '''Config controller'''
    
    def __init__(self, config_service: ConfigService):
        self._service = config_service

    async def write_app_config(self, app_config:AppConfigRequest):
        '''Changing configuration for application section'''
        try:
            config = app_config.model_dump()
            await self._service.write_app(**config)                            
        except Exception as ex:
            raise HTTPException(status_code=401, detail=ex)
      
    async def write_jwt_auth_config(self, jwt_auth: JwtAuthConfigRequest):
        '''Changing configuration for JwtAuth section'''
        try:
            jwt_config = jwt_auth.model_dump()
            await self._service.write_jwt_auth(**jwt_config)            
        except Exception as ex:
            raise HTTPException(status_code=401, detail=ex)
    
    async def write_mail_config(self, mail: MailConfigRequest):
        'Update mail config'
        try:
            mail_config = mail.model_dump()            
            await self._service.write_email(**mail_config)            
        except Exception as ex:
            raise HTTPException(status_code=401, detail=ex)
            
    async def write_db_context_config(self, db_context: DbContextConfigRequest):
        '''Changing configuration for DbContext section'''
        try:
            _config = db_context.model_dump()

            await self._service.write_db_context(**_config)            
        except Exception as ex:
            raise HTTPException(status_code=401, detail=ex)
      
    async def write_logging_config(self, log_config: LoggingConfigRequest = LoggingConfigRequest(directory="/app/logs", level="DEBUG", filename_suffix="app")):
        '''Changing configuration for Logging section'''
        try:
            _config = log_config.model_dump()
            await self._service.write_logging(**log_config)
        except Exception as ex:
            raise HTTPException(status_code=401, detail=ex)
    
    async def get_all_config(self):
        ''' Get all config '''
        try :
            return await self._service.get_all_config()
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
        