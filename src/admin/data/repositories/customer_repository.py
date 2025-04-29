from logger import AppLogger
from data.db_context import DbContext, DataOperators
from admin.data.entities.customer import Customer
from helper import helper
from typing import List

class CustomerRepository():
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must be a part of DataOperators"))
        self.db_context = db_context
        
    async def get_all_customer(self) -> List[Customer]:
        '''get all info customer '''
        try:
            query = """SELECT cus_code,cus_name FROM Customer """
            customers = await self.db_context.get_data(query)
            return [Customer(**c) for c in customers]
        except Exception as ex:
            self._logger.error(f"get customers error {ex}")
            
            
    async def get_customer(self, code) -> Customer:
        '''get detail customer '''
        try:
            query = """SELECT cus_code, cus_name FROM Customer WHERE upper(cus_code) = upper(:V_CODE)"""
            customer = await self.db_context.get_data(query, {"V_CODE": code})
            return Customer(**customer[0]) if customer else Customer.empty()
        except Exception as ex:
            self._logger.error(f"get customer error {ex}")
            
    
    async def add(self, entity: Customer):
        '''Add new customer'''
        try:
            query = """ INSERT INTO Customer(CUS_CODE, CUS_NAME, CUS_CREATED_UTC, CUS_UPDATED_UTC )
                        VALUES(  :V_CODE, 
                                :V_NAME,
                                TO_DATE(:V_CREATED_ON_UTC, 'DD/MM/YYYY HH24:MI:SS'),
                                TO_DATE(:V_UPDATED_ON_UTC, 'DD/MM/YYYY HH24:MI:SS')
                    )"""
            date = helper.get_date_utc()
            return await self.db_context.execute_query(query, {
                "V_CODE": entity.Code,
                "V_NAME": entity.Name,
                "V_CREATED_ON_UTC": date,
                "V_UPDATED_ON_UTC": date,
            })
        except Exception as ex:
            self._logger.error(f"Add error {ex}")
    
    async def update(self, id, entity: Customer):
        'Update customer'
        try:
            query = """UPDATE Customer
                SET CUS_NAME = :V_NAME, 
                    CUS_UPDATED_UTC = TO_DATE(:V_UPDATED_ON_UTC, 'DD/MM/YYYY HH24:MI:SS')
                WHERE CUS_CODE = :V_CODE"""
            return await self.db_context.execute_query(query, {
                "V_CODE": id,
                "V_NAME": entity.Name,
                "V_UPDATED_ON_UTC": helper.get_date_utc()
            })
        except Exception as ex:
            self._logger.error(f"Update error {ex}")

    async def delete(self, id):
        'Delete customer'
        try:
            query = """DELETE FROM Customer WHERE CUS_CODE = :V_CODE
                AND NOT EXISTS (SELECT NULL FROM AWR_REPO_INFO WHERE CUS_CODE = :V_CODE)"""
            return await self.db_context.execute_query(query, {"V_CODE": id})
        except Exception as ex:
            self._logger.error(f"Delete error {ex}")
    
    async def clear_all(self):
        '''Delete all SQL Configuration
        '''
        try:
            query = "TRUNCATE TABLE Customer"
            return await self.db_context.execute_query(query)
        except Exception as ex:
            self._logger.error(f"clean SYS_MENU failed. \nError: {ex}")