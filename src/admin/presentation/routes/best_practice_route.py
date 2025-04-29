from fastapi import APIRouter, Depends, HTTPException
from admin.factory import AdminFactory
from admin.services.best_practice_service import BestPracticeService
from dependencies import get_admin_factory
from admin.models.response_model import successful, failed
from admin.presentation.controller import BestPracticeController
from admin.models.request_model import BestPracticeRequest
from app.presentation.route import verify_auth

best_practice_router = APIRouter(tags=["Best Practice"],)

def get_best_practice_controller(admin_factory: AdminFactory = Depends(get_admin_factory)):
    '''Get  Best Practice controller'''
    return BestPracticeController(BestPracticeService(admin_factory))

@best_practice_router.post("/get-all", response_model=None)
async def get_all(controller: BestPracticeController = Depends(get_best_practice_controller)):
    '''Get all best practices'''
    try:
        return await controller.get_all()
    except Exception as ex:
        return failed(f"{ex}")

@best_practice_router.get("/show/{id}", response_model=None)
async def show(id:int, controller: BestPracticeController = Depends(get_best_practice_controller)):
    '''Show best practice by ID'''
    try:
        return await controller.get_by_id(id)
    except Exception as ex: 
        return failed(f"{ex}")

@best_practice_router.post("/add", response_model=None)
async def add(request: BestPracticeRequest, controller: BestPracticeController = Depends(get_best_practice_controller)):
    '''Add best practice'''
    try:
        result = await controller.add(request)
        return successful if result == 0 else failed("Add best practice failed")
    except Exception as ex:
        return failed(f"{ex}")

@best_practice_router.put("/update/{id}", response_model=None)
async def update(id:int, request: BestPracticeRequest, controller: BestPracticeController = Depends(get_best_practice_controller)):
    '''Update best practice'''
    try:
        result = await controller.update(id, request)
        return successful if result == 0 else failed("Update best practice failed")
    except Exception as ex:
        return failed(f"{ex}")

@best_practice_router.delete("/delete/{id}", response_model=None)
async def delete(id:int, controller: BestPracticeController = Depends(get_best_practice_controller)):
    '''Delete best practice'''
    try:
        result = await controller.delete(id)
        return successful if result == 0 else failed("Delete best practice failed")
    except Exception as ex:
        return failed(f"{ex}")
