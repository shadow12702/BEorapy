from logger import AppLogger
from data.db_context import DbContext, DataOperators
from admin.data.entities.patch import Patch
from typing import List

class PatchRepository():
    _logger = AppLogger().get_logger()

    def __init__(self, db_context: DbContext):
        if not isinstance(db_context, DataOperators):
            self._logger.error("db_context must be a part of DataOperators")
            raise TypeError("db_context must be a part of DataOperators")
        self.db_context = db_context

    async def get_patch(self) -> List[Patch]:
        '''Get all info PATCH '''
        try:
            query = """ SELECT * FROM SYS_PATCH """
            awr_data = await self.db_context.get_data(query)
            return [Patch(**c) for c in awr_data] 
        except Exception as ex:
            self._logger.error(f"get SysPatch error {ex}")
            return []

    async def get_patch_by_id(self, id : int) -> Patch:
        '''Get detail Patch by PATCH_ID'''
        try:
            query = """SELECT DB_VERSION, TYPE, FORMAT, PATCH_ROOT, PATCH_ID, PATCH_TYPE, 
                              FIXED_IN_RU, FIXED_IN_MRP, DESCRIPTION
                       FROM SYS_PATCH 
                       WHERE PATCH_ID = :V_ID"""
            patch_data = await self.db_context.get_data(query, {"V_ID": id})
            return Patch(**patch_data[0]) if patch_data else None
        except Exception as ex:
            self._logger.error(f"get Patch by ID error {ex}")
            return None

    async def add(self, entity: Patch):
        '''Add new Patch'''
        try:
            query = """ INSERT INTO SYS_PATCH (DB_VERSION, TYPE, FORMAT, PATCH_ROOT, PATCH_ID, PATCH_TYPE,FIXED_IN_RU, FIXED_IN_MRP, DESCRIPTION )
                        VALUES (:V_DB_VERSION, :V_TYPE, :V_FORMAT, :V_PATCH_ROOT, :V_PATCH_ID, :V_PATCH_TYPE, :V_FIXED_IN_RU, :V_FIXED_IN_MRP, :V_DESCRIPTION) """
            return await self.db_context.execute_query(query, {
                "V_DB_VERSION": entity.DbVersion,
                "V_TYPE": entity.Type,
                "V_FORMAT": entity.Format,
                "V_PATCH_ROOT": entity.Root,
                "V_PATCH_ID": entity.Id,
                "V_PATCH_TYPE": entity.PatchType,
                "V_FIXED_IN_RU": entity.FixedInRu,
                "V_FIXED_IN_MRP": entity.FixedInMRP,
                "V_DESCRIPTION": entity.Description,
            })
        except Exception as ex:
            self._logger.error(f"Add Patch error {ex}")
            return None

    async def update(self, id:int, entity: Patch):
        '''Update Patch by PATCH_ID'''
        try:
            query = """UPDATE SYS_PATCH
                       SET DB_VERSION = :V_DB_VERSION, 
                           TYPE = :V_TYPE, 
                           FORMAT = :V_FORMAT, 
                           PATCH_ROOT = :V_PATCH_ROOT, 
                           PATCH_TYPE = :V_PATCH_TYPE, 
                           FIXED_IN_RU = :V_FIXED_IN_RU,
                           FIXED_IN_MRP = :V_FIXED_IN_MRP,
                           DESCRIPTION = :V_DESCRIPTION
                       WHERE PATCH_ID = :V_PATCH_ID"""
            return await self.db_context.execute_query(query, {
                "V_DB_VERSION": entity.DbVersion,
                "V_TYPE": entity.Type,
                "V_FORMAT": entity.Format,
                "V_PATCH_ROOT": entity.Root,
                "V_PATCH_ID": id,
                "V_PATCH_TYPE": entity.PatchType,
                "V_FIXED_IN_RU": entity.FixedInRu,
                "V_FIXED_IN_MRP": entity.FixedInMRP,
                "V_DESCRIPTION": entity.Description,
            })
        except Exception as ex:
            self._logger.error(f"Update Patch error {ex}")
            return None
