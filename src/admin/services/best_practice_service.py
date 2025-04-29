from admin.models.response_model import BestPracticeResponse
from admin.data.entities.best_practice import BestPractice
from admin.factory import AdminFactory
from logger import AppLogger

class BestPracticeService():    
    _logger = AppLogger().get_logger()

    def __init__(self, admin_factory: AdminFactory):
        self.repository = admin_factory.best_practice_repository()

    async def get_all(self):
        try:
            all_practices = await self.repository.get_all()
            result = [
                BestPracticeResponse(**{
                    "id": item.Id,
                    "db_version": item.DbVersion,  
                    "parameter": item.Parameter,
                    "param_default_value": item.ParamDefaultValue,
                    "param_recommend_value": item.ParamRecommendValue,
                    "for_rac_only": item.ForRacOnly,
                    "notes": item.Notes,
                }) 
                for item in all_practices
            ]
            return result
        except Exception as ex:
            self._logger.error(f"Get best practices error: {ex}")
            raise ex
    
    async def get_by_id(self, id:int):
        try:
            ''' Show best practice by ID '''
            practice = await self.repository.get_by_id(id)
            result = [
                BestPracticeResponse(**{
                    "id": item.Id,
                    "db_version": item.DbVersion,  
                    "parameter": item.Parameter,
                    "param_default_value": item.ParamDefaultValue,
                    "param_recommend_value": item.ParamRecommendValue,
                    "for_rac_only": item.ForRacOnly,
                    "notes": item.Notes,
                }) 
                for item in practice
            ]
            return result
        except Exception as ex:
            self._logger.error(f"Get best practices error: {ex}")
            raise ex

    async def add(self, entity: BestPractice):
        ''' Add best practice '''
        return await self.repository.add(entity)

    async def update(self, id:int, entity: BestPractice):
        ''' Update best practice '''
        return await self.repository.update(id, entity)
    
    async def delete(self, id:int):
        ''' Delete best practice '''
        return await self.repository.delete(id)
