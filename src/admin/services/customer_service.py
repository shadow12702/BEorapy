from admin.models.request_model import CustomerRequest
from admin.models.response_model import CustomerResponse
from admin.data.entities.customer import Customer
from admin.factory import AdminFactory
from logger import AppLogger

class CustomerService():    
    _logger = AppLogger().get_logger()

    def __init__(self, admin_factory: AdminFactory):
        self.repository = admin_factory.customers_repository()

    async def get_all_customers(self):
        try:
            all_customers = await self.repository.get_all_customer()
            result = [
                CustomerResponse(**item.to_response()) 
                for item in all_customers
            ]
            return result
        except Exception as ex:
            self._logger.error(f"get customers error : {ex}")
            raise ex
    
        
    async def get_customer(self,code):
        ''' Show customer'''
        customer = await self.repository.get_customer(code)
        result =  CustomerResponse(**customer.to_response()) 
        return result


    async def add(self, entity: CustomerRequest):
        ''' Add customers
            
            :param entity
            '''
        
        return await self.repository.add(entity)


    async def update (self, code , entity:Customer ):
        '''Update menu'''
        return await self.repository.update(code, entity)
    

    async def delete(self, code):
        ''' Delete menu'''
        return await self.repository.delete(code)