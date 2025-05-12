from fastapi import APIRouter, Depends
from admin.factory import AdminFactory
from admin.services.customer_service import CustomerService
from dependencies import get_admin_factory
from admin.models.response_model import successful, failed
from admin.presentation.controller import CustomerController
from admin.models.request_model import CustomerRequest
from admin.models.request_model import UpdateCustomerRequest
from app.presentation.route import verify_auth

customer_router = APIRouter(tags=["Customer"], dependencies=[Depends(verify_auth)])

def get_customer_controller(admin_factory: AdminFactory = Depends(get_admin_factory)):
    '''Get customer controller'''
    return CustomerController(CustomerService(admin_factory))

@customer_router.post("/get-customer", response_model=None)
async def get_customer(controller: CustomerController = Depends(get_customer_controller)):
    '''Get customer by request'''
    try:
        return await controller.get_all_customer()  
    except Exception as ex:
        return failed(f"{ex}")
    
    
    
@customer_router.get("/show/{code}" , response_model=None)
async def show(code , controller: CustomerController = Depends(get_customer_controller)):
    '''Show detail customer'''
    try:
        return await controller.get_customer(code)
    except Exception as ex:
        return failed(f"{ex}")
    
    
    
@customer_router.post("/add", response_model=None)
async def add(customer: CustomerRequest, controller: CustomerController = Depends(get_customer_controller)):
    '''Add customer'''
    try:
        result = await controller.add_customer(customer)
        return successful if result == 0 else failed("Add customer failed")
    except Exception as ex:
        return failed(f"{ex}")
    

@customer_router.put("/update/{code}", response_model=None)
async def update(code, customer: UpdateCustomerRequest , controller: CustomerController = Depends(get_customer_controller)):
    '''Update customer'''
    try:
        result = await controller.update_customer(code, customer)
        return successful if result == 0 else failed("Update customer failed")
    except Exception as ex:
        return failed(f"{ex}")
    
    
    
@customer_router.delete("/delete/{code}", response_model=None)
async def delete(code, controller: CustomerController = Depends(get_customer_controller)):
    '''Delete customer'''
    try:
        result = await controller.delete_customer(code)
        return successful if result == 0 else failed("Delete customer failed")
    except Exception as ex:
        return failed(f"{ex}")
