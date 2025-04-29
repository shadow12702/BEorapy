from fastapi import APIRouter, Depends
from admin.factory import AdminFactory
from admin.services.config_service import ConfigService
from dependencies import get_admin_factory, config_manager as cf_manager
from admin.models.request_model import AppConfigRequest, DbContextConfigRequest, JwtAuthConfigRequest, LoggingConfigRequest, MailConfigRequest,ConfigRequest
from admin.models.response_model import successful, failed
from admin.presentation.controller import ConfigController
from app.presentation.route import verify_auth

config_router = APIRouter(tags=["Configuration"], dependencies=[Depends(verify_auth)])

def get_config_controller(admin_factory: AdminFactory = Depends(get_admin_factory)):
    '''Get config controller'''
    return ConfigController(ConfigService(admin_factory))

@config_router.post("/app-config", response_model=None)
async def app_config(app: AppConfigRequest,
                     config_controller: ConfigController = Depends(get_config_controller)):
    try:
        await config_controller.write_app_config(app)
        await cf_manager.reload_config()
        return successful
    except Exception as ex:
        return failed(ex)
    
@config_router.post("/jwt-auth", response_model=None)
async def jwt_config(jwt_auth: JwtAuthConfigRequest,
                     config_controller: ConfigController = Depends(get_config_controller)):
    try:
        await config_controller.write_jwt_auth_config(jwt_auth)
        await cf_manager.reload_config()
        return successful
    except Exception as ex:
        return failed(ex)


@config_router.post("/mail-config", response_model=None)
async def mail_config(mail: MailConfigRequest,
                     config_controller: ConfigController = Depends(get_config_controller)):
    try:
        await config_controller.write_mail_config(mail)
        await cf_manager.reload_config()
        return successful
    except Exception as ex:
        return failed(ex)

@config_router.post("/db-context", response_model=None)
async def db_config(config: DbContextConfigRequest,
                    config_controller: ConfigController = Depends(get_config_controller)):
    try:
        await config_controller.write_db_context_config(config)
        return successful
    except Exception as ex:
        return failed(ex)


@config_router.post("/logging", response_model=None)
async def logging_config(config: LoggingConfigRequest,config_controller: ConfigController = Depends(get_config_controller)):
    try:
        await config_controller.write_logging_config(config)
        return successful
    except Exception as ex:
        return failed(ex)
    
@config_router.post("/get-all" , response_model = None)
async def get_all_config(controller : ConfigController = Depends(get_config_controller)):
    try:
        return await controller.get_all_config()  
    except Exception as ex:
        return failed(f"{ex}")

@config_router.post("/add", response_model=None)
async def add(config: ConfigRequest, controller: ConfigController = Depends(get_config_controller)):
    '''Add config'''
    try:
        result = await controller.add_config(config)
        return successful if result == 0 else failed("Add config failed")
    except Exception as ex:
        return failed(f"{ex}")

@config_router.put("/update/{type}/{key}", response_model=None)
async def update(type:str , key:str , config: ConfigRequest, controller: ConfigController = Depends(get_config_controller)):
    '''Update config'''
    try:
        result = await controller.update_config(key , type , config)
        return successful if result == 0 else failed("Update config failed")
    except Exception as ex:
        return failed(f"{ex}")
