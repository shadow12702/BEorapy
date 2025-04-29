from fastapi import APIRouter, Depends
from admin.factory import AdminFactory
from dependencies import get_admin_factory
from admin.presentation.controller import PatchController
from admin.services.patch_service import PatchService
from admin.models.response_model import successful, failed
from admin.models.request_model import PatchRequest,PatchUpdateRequest

patch_router = APIRouter(tags=["Patch"])

def get_patch_controller(admin_factory: AdminFactory = Depends(get_admin_factory)):
    '''Get tem Patch controller'''
    return PatchController(PatchService(admin_factory))

@patch_router.post("/get-patch", response_model=None)
async def get_patch(controller: PatchController = Depends(get_patch_controller)):
    '''Get tem Patch by request'''
    try:    
        return await controller.get_patch()  
    except Exception as ex:
        return failed(f"{ex}")



@patch_router.post("/add", response_model=None)
async def add(patch: PatchRequest, controller: PatchController = Depends(get_patch_controller)):
    '''Add a new tem Patch'''
    try:
        result = await controller.add_patch(patch)
        return successful if result == 0 else failed("Add tem patch failed")
    except Exception as ex:
        return failed(f"{ex}")
    
    
    
@patch_router.get("/show/{id}", response_model=None)
async def show(id: int, controller: PatchController = Depends(get_patch_controller)):
    
    '''Show tem Patch details by ID'''
    try:
        return await controller.get_patch_by_id(id)
    except Exception as ex:
        return failed(f"{ex}")
    


@patch_router.put("/update/{id}", response_model=None)
async def update(id: int, patch: PatchUpdateRequest, controller: PatchController = Depends(get_patch_controller)):
    '''Update tem Patch details by ID'''
    try:
        result = await controller.update_patch(id, patch)
        return successful if result == 0 else failed("Update tem patch failed")
    except Exception as ex:
        return failed(f"{ex}")

