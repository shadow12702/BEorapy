from fastapi import APIRouter, Depends
from admin.factory import AdminFactory
from admin.services.menu_service import MenuService
from dependencies import get_admin_factory
from admin.models.request_model import MenuRequest, MenuTypeRequest
from admin.models.response_model import successful, failed
from admin.presentation.controller import MenuController
from app.presentation.route import verify_auth

menu_router = APIRouter(tags=["Menu"], dependencies=[Depends(verify_auth)])

def get_menu_controller(admin_factory: AdminFactory = Depends(get_admin_factory)):
    '''Get menu controller'''
    return MenuController(MenuService(admin_factory))

@menu_router.post("/get-menu", response_model=None, dependencies=[Depends(verify_auth)])
async def get_menu(menu_type: MenuTypeRequest, controller: MenuController = Depends(get_menu_controller)):
    '''Get menu'''
    try:
        return await controller.get_menu(menu_type)
    except Exception as ex:
        return failed(f"{ex}")

@menu_router.post("/add", response_model=None, dependencies=[Depends(verify_auth)])
async def add(menu: MenuRequest,  controller: MenuController= Depends(get_menu_controller)):
    '''Add menu'''
    try:
        result = await controller.add_menu(menu)
        return successful if result == 0 else failed("Add menu failed")
    except Exception as ex:
        return failed(f"{ex}")

@menu_router.put("/update/{id}", response_model=None, dependencies=[Depends(verify_auth)])
async def update(id: int, menu: MenuRequest,  controller: MenuController= Depends(get_menu_controller)):
    '''Update menu'''
    try:
        result = await controller.update_menu(id, menu)
        return successful if result == 0 else failed("Update menu failed")
    except Exception as ex:
        return failed(f"{ex}")
    
@menu_router.delete("/delete/{id}", response_model=None, dependencies=[Depends(verify_auth)])
async def delete(id: int,  controller: MenuController= Depends(get_menu_controller)):
    '''Delete menu'''
    try:
        result = await controller.delete_menu(id)
        return successful if result == 0 else failed("Delete menu failed")
    except Exception as ex:
        return failed(f"{ex}")

