# Description: MenuService

from typing import List
from logger import AppLogger
from admin.data.entities.menu import Menu
from admin.factory import AdminFactory
from admin.models.response_model import MenuResponse


class MenuService():

    _logger = AppLogger().get_logger()
    
    def __init__(self, repo_factory: AdminFactory):
        self.repository = repo_factory.menu_repository()
    
    async def get_menu(self, type: int):
        '''Get all menu

        :return: List of all menu'''
        try:
            menu =  await self.repository.get_menu(type)
            result = [MenuResponse.from_model(item) for item in menu ]
            return result
        except Exception as ex:
            self._logger.error(f"get menu error: {ex}")
            raise ex

    async def add(self, entity: Menu):
        '''Add menu

        :param entity: Menu model'''
        return await self.repository.add(entity)
        
    async def add_many(self, entities: List[Menu]):
        '''Add multiple menu 

        :param entities: List of menu'''
        try:
            data = [(e.name, e.icon, e.parent, e.prefix, e.route, e.is_show) for e in entities]
            return await self.repository.add_many(data)
        except Exception as ex:
            self._logger.error(f"addMany Menus error: \n{entities.__repr__()}\n{ex}")
        
    async def update(self, id: int, entity: Menu):
        '''Update menu

        :param id: id of menu will be updated
        :param entity: new menu information need to update'''
        return await self.repository.update(id, entity)
        
    
    async def delete(self, id: int):
        '''Delete menu

        :param id: Id of the menu will be deleted'''
        return await self.repository.delete(id)
        
    