from fastapi import APIRouter, Depends
from app.factory import ApplicationFactory
from dependencies import get_app_factory
from app.models.request_model import AshOverallRequest
from app.models.response_model import successful, failed
from app.presentation.controller import CdbAshOverallController
from app.services.cdb_ash_overall_service import CdbAshOverallService
from app.presentation.route import verify_auth

cdb_ash_overall_router = APIRouter(tags=["CDB ASH Overall"], dependencies=[Depends(verify_auth)])

def get_menu_controller(app_factory: ApplicationFactory = Depends(get_app_factory)):
    '''Get menu controller'''
    return CdbAshOverallController(CdbAshOverallService(app_factory))

@cdb_ash_overall_router.post("/get-ash-overall-table", response_model=None)
async def get_ash_overall_table(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_table(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")


@cdb_ash_overall_router.post("/get-ash-overall-index", response_model=None)
async def get_ash_overall_index(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_index(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")


@cdb_ash_overall_router.post("/get-ash-overall-segment", response_model=None)
async def get_ash_overall_segment(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_segment(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")


@cdb_ash_overall_router.post("/get-ash-overall-wait-class", response_model=None)
async def get_ash_overall_wait_class(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_wait_class(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")


@cdb_ash_overall_router.post("/get-ash-overall-event", response_model=None)
async def get_ash_overall_event(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_event(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")

@cdb_ash_overall_router.post("/get-ash-overall-module", response_model=None)
async def get_ash_overall_module(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_module(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")


@cdb_ash_overall_router.post("/get-ash-overall-program", response_model=None)
async def get_ash_overall_progra(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_program(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")

@cdb_ash_overall_router.post("/get-ash-overall-sql-cpu", response_model=None)
async def get_ash_overall_sql_cpu(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_sql_cpu(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")


@cdb_ash_overall_router.post("/get-ash-overall-sql-operation", response_model=None)
async def get_ash_overall_sql_operation(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_sql_operation(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")

@cdb_ash_overall_router.post("/get-ash-overall-sql-io", response_model=None)
async def get_ash_overall_sql_io(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_sql_io(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")


@cdb_ash_overall_router.post("/get-ash-overall-event", response_model=None)
async def get_ash_overall_event(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_event(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")

@cdb_ash_overall_router.post("/get-ash-overall-wait", response_model=None)
async def get_ash_overall_wait(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_wait(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")


@cdb_ash_overall_router.post("/get-ash-overall-wait-global", response_model=None)
async def get_ash_overall_wait_global(ash_overall_request: AshOverallRequest, controller: CdbAshOverallController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_ash_overall_wait_global(ash_overall_request)
    except Exception as ex:
        return failed(f"{ex}")
