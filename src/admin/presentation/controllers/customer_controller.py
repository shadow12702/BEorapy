from fastapi import HTTPException
from admin.services.customer_service import CustomerService
from admin.models.request_model import CustomerRequest
from admin.models.request_model import UpdateCustomerRequest
from admin.data.entities.customer import Customer
 
class CustomerController:
    '''Customer Controller'''

    def __init__(self, customer_service: CustomerService):
        self._service = customer_service

    async def get_all_customer(self):
        '''Get all customers based on request'''
        customers = await self._service.get_all_customers()
        return customers


    async def get_customer(self, code):
        '''Show detail customer'''
        try:
            customer = await self._service.get_customer(code)
            return customer
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}" )
    
    

    async def add_customer(self, customer_request: CustomerRequest):
        '''Add customer'''
        try:
            request = customer_request.model_dump()
            customer = Customer(**request)
            return await self._service.add(customer)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
        


    async def update_customer(self, code, customer_request: UpdateCustomerRequest):
        '''Update customer'''
        try:
            request = customer_request.model_dump()
            customer = Customer(**request)
            return await self._service.update( code , customer )
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    
    
    async def delete_customer(self, code):
        '''Delete customer'''
        try:
            return await self._service.delete(code)
        except Exception as ex:
            raise HTTPException(status_code=400, deltal = f"{ex}")