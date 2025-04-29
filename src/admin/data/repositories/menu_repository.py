from logger import AppLogger
from helper import helper
from data.db_context import DbContext, DataOperators
from admin.data.entities.menu import Menu
from typing import List

class MenuRepository():
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must be a part of DataOperators"))
        self.db_context = db_context

    async def get_menu(self, admin_site: int=0) -> List[Menu]:
        '''Get list menu info by type

        :return: list menu'''
        try:            
            query = """SELECT * FROM SYS_MENU WHERE MN_ADMIN_SITE = :V_ADMIN_SITE ORDER BY ID"""
            data = await self.db_context.get_data(query, {"V_ADMIN_SITE" : admin_site})
            result = [Menu(**e) for e in data]
            return result
        except Exception as ex:
            self._logger.error(f"getMenu error {ex}")
    
    async def add(self, entity: Menu):
        '''Add new menu'''
        try:
            query = """INSERT INTO SYS_MENU(MN_CODE, MN_NAME, MN_ICON, MN_PARENT, MN_LINK, MN_ADMIN_SITE, CREATED_ON_UTC, UPDATED_ON_UTC)
                    VALUES(:V_CODE, :V_NAME, :V_ICON, :V_PARENT, :V_LINK, :V_ADMIN_SITE,
                    TO_DATE(:V_CREATED_ON_UTC, 'DD/MM/YYYY HH24:MI:SS'),
                    TO_DATE(:V_UPDATED_ON_UTC, 'DD/MM/YYYY HH24:MI:SS')
                    )"""
            date = helper.get_date_utc()
            return await self.db_context.execute_query(query, {
                "V_CODE": entity.Code,
                "V_NAME": entity.Name,
                "V_ICON": entity.Icon,
                "V_PARENT": entity.Parent,
                "V_LINK": entity.Route,
                "V_ADMIN_SITE": entity.AdminSite,
                "V_CREATED_ON_UTC": date,
                "V_UPDATED_ON_UTC": date
            })
        except Exception as ex:
            self._logger.error(f"Add error {ex}")
    
    async def update(self, id: int, entity: Menu):
        'Update menu'
        try:
            query = """UPDATE SYS_MENU
                SET MN_NAME = :V_NAME, 
                    MN_ICON = :V_ICON, 
                    MN_PARENT = :V_PARENT, 
                    MN_LINK = :V_LINK,
                    MN_ADMIN_SITE = :V_ADMIN_SITE,
                    UPDATED_ON_UTC = TO_DATE(:V_UPDATED_ON_UTC, 'DD/MM/YYYY HH24:MI:SS')
                WHERE ID = :V_ID"""
            return await self.db_context.execute_query(query, {
                "V_ID": id,
                "V_NAME": entity.Name,
                "V_ICON": entity.Icon,
                "V_PARENT": entity.Parent,
                "V_LINK": entity.Route,
                "V_ADMIN_SITE": entity.AdminSite,
                "V_UPDATED_ON_UTC": helper.get_date_utc()
            })
        except Exception as ex:
            self._logger.error(f"Update error {ex}")

    async def delete(self, id: int):
        'Delete menu'
        try:
            query = "DELETE FROM SYS_MENU WHERE ID = :V_ID"
            return await self.db_context.execute_query(query, {"V_ID": id})
        except Exception as ex:
            self._logger.error(f"Delete error {ex}")
    
    async def clear_all(self):
        '''Delete all SQL Configuration
        '''
        try:
            query = "TRUNCATE TABLE SYS_MENU"
            return await self.db_context.execute_query(query)
        except Exception as ex:
            self._logger.error(f"clean SYS_MENU failed. \nError: {ex}")