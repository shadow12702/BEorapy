from fastapi import HTTPException
from admin.data.entities.menu import Menu
from helper import helper
from admin.services.menu_service import MenuService
from admin.models.request_model import MenuRequest, MenuTypeRequest

class MenuController:
    '''Menu controller'''
    
    def __init__(self, menu_service: MenuService):
        self._service = menu_service

    async def get_menu(self, menu_type_request: MenuTypeRequest):
        '''Get all menu

        :return: List of all menu'''
        return await self._service.get_menu(menu_type_request.type)
    
    async def add_menu(self, menu_request: MenuRequest):
        try:
            request = menu_request.model_dump()
            menu = Menu(**request)
            
            if not helper.strNotEmpty(menu.Name):
                raise HTTPException(status_code=400, detail="Name is required")
            
            return await self._service.add(menu)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def update_menu(self, id: int, menu_request: MenuRequest):
        '''Update menu'''
        try:
            request = menu_request.model_dump()
            menu = Menu(**request)

            if not helper.strNotEmpty(menu.Name):
                raise HTTPException(status_code=400, detail="Name is required")
            
            return await self._service.update(id, menu)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def delete_menu(self, id: int):
        '''Delete menu'''
        try:
            return await self._service.delete(id)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")