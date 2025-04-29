from numpy import int64
from logger import AppLogger
from app.data.repositories.enum.addm_enum import AddmEnum
from app.data.entities.addm.writing_recommendations import WritingRecommendations
from data.db_context import DbContext, DataOperators
from app.data.repositories.general_repository import GeneralRepository


class AddmRepository(GeneralRepository):

    _logger = AppLogger().get_logger()

    def __init__(self, db_context: DbContext):
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must implement DataOperations"))    
        self.db_context = db_context        
    
    def getWritingRecommendations(self, dbid:int64, begin_snap: int64, end_snap: int64):
        '''Method to retrieve data for WritingRecommendations object.
        
        Args:
            dbid: Database ID
            begin_snap: Begin snapshot
            end_snap: End snapshot
        
        Return: 
            List of WritingRecommendations or an empty list
        '''
        try:             
            return self.getValue(AddmEnum.WRITING_RECOMMENDATIONS, WritingRecommendations, dbid, begin_snap, end_snap)
            # query = self.redis.getKey(AddmEnum.WRITING_RECOMMENDATIONS.value)
            # data = self.db_context.getData(
            #     query=query,
            #     params={'P_DBID': dbid,                                                    
            #             "P_BEGIN_SNAP":begin_snap, 
            #             "P_END_SNAP":end_snap
            #             }
            #     )
            # entities = [WritingRecommendations(**e) for e in data] if data else List[WritingRecommendations.empty()]
            # return entities
        except Exception as ex:
            self._logger.error(f"get WritingRecommendations error: {ex}")
            
    def startAnalysis(self, dbid:int64, begin_snap: int64, end_snap: int64):
        '''Analysis ADDM to retrieve data for WritingRecommendations object.
        
        Args:
            dbid: Database ID
            begin_snap: Begin snapshot
            end_snap: End snapshot        
        '''
        try:
            query = self.redis.getKey(AddmEnum.STARTING_ANALYSIS.value)
            data = self.db_context.callPlSql(plsql=query, 
                                             input_params={'P_DBID': dbid,
                                                           "P_BEGIN_SNAP":begin_snap, 
                                                           "P_END_SNAP":end_snap
                                                           }
                                             )
            return data
        except Exception as ex:
            self._logger.error(f"startAnalysis error: {ex}")
    
    def dropRecommendations(self, dbid:int64, begin_snap: int64, end_snap: int64):
        '''Clearing ADDM 
        
        Args:
            dbid: Database ID
            begin_snap: Begin snapshot
            end_snap: End snapshot        
        '''
        try:
            query = self.redis.getKey(AddmEnum.DROP_RECOMMENDATIONS.value)
            data = self.db_context.callPlSql(plsql=query, 
                                             input_params={'P_DBID': dbid,
                                                           "P_BEGIN_SNAP":begin_snap, 
                                                           "P_END_SNAP":end_snap
                                                           }
                                             )
            return data
        except Exception as ex:
            self._logger.error(f"dropRecommendations error: {ex}")
            return ''
        