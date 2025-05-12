from fastapi import HTTPException
from admin.services.patch_service import PatchService
from admin.models.request_model import PatchRequest


class PatchController:
    def __init__(self , patch_service: PatchService):
        self._service = patch_service
    
    async def get_patch(self):
        '''Get all patch'''
        all_patch = await self._service.get_patch()
        return all_patch
    
    async def get_patch_by_id(self, id:int):
        '''Show detail patch'''
        try:
            patch = await self._service.get_patch_by_id(id)
            return patch
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}" )
    

    async def add_patch(self,patch_request: PatchRequest):
        '''Add patch'''
        try:
            return await self._service.add(patch_request)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
        
