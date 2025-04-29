from fastapi import HTTPException
from admin.services.best_practice_service import BestPracticeService
from admin.models.request_model import BestPracticeRequest
from admin.data.entities.best_practice import BestPractice

class BestPracticeController:
    ''' Best Practice Controller'''

    def __init__(self, service: BestPracticeService):
        self._service = service

    async def get_all(self):
        '''Get all best practices'''
        practices = await self._service.get_all()
        return practices

    async def get_by_id(self, id:int):
        '''Show best practice by ID'''
        try:
            practice = await self._service.get_by_id(id)
            return practice
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def add(self, request: BestPracticeRequest):
        '''Add best practice'''
        try:
            practice1 = request.model_dump()
            practice = BestPractice(**request.model_dump())
            return await self._service.add(practice)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def update(self, id, request: BestPracticeRequest):
        '''Update best practice'''
        try:
            
            practice = BestPractice(**request.model_dump())
            return await self._service.update(id, practice)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def delete(self, id):
        '''Delete best practice'''
        try:
            return await self._service.delete(id)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
