from admin.models.response_model import PatchResponse
from admin.factory import AdminFactory
from admin.data.entities.patch import Patch
from admin.models.request_model import PatchRequest

from logger import AppLogger

class PatchService():
    _logger = AppLogger().get_logger()
    
    def __init__(self , admin_factory: AdminFactory):
        self.repository = admin_factory.patch_repository()
        
    async def get_patch(self):
        try:
            all_patches = await self.repository.get_patch()
            result = [
                PatchResponse(**item.to_response()) for item in all_patches
            ]
            return result
        except Exception as ex:
            self._logger.error(f"get System Patch error: {ex}")
            raise ex
        
    async def get_patch_by_id(self, id):
        '''Show patch by id'''
        try:
            patch = await self.repository.get_patch_by_id(id)
            if patch:
                result = PatchResponse(**patch.to_response())
                return result
            else:
                return None
        except Exception as ex:
            self._logger.error(f"get Patch by ID error: {ex}")
            raise ex
    
    async def add(self, entity : PatchRequest):
        '''Add new Patch'''
        try:
            # Assuming 'entity' is a Patch object.
            request = entity.model_dump()
            patch = Patch.from_dict(request)
            return await self.repository.add(patch)
        except Exception as ex:
            self._logger.error(f"Add Patch error: {ex}")
            raise ex

