# Description: 

from numpy import int64
from app.factory import ApplicationFactory
from logger import AppLogger

class AddmService():
        
    _logger = AppLogger().get_logger()
    
    def __init__(self, repo_factory: ApplicationFactory):        
        self.addmRepository = repo_factory.addmRepository()        
    
    def addmProcess(self, dbid:int64, begin_snap:int64, end_snap: int64):
        '''
        Addm Processing 
        
        :return : list WritingRecommendations 
        '''
        try:
            # start analysis
            self.addmRepository.startAnalysis(dbid = dbid,
                                              begin_snap = begin_snap, 
                                              end_snap = end_snap)
            # get data for writing recommendations
            data = self.addmRepository.getWritingRecommendations(dbid = dbid,
                                                                 begin_snap = begin_snap,
                                                                 end_snap= end_snap)
            # delete recommendations
            self.addmRepository.dropRecommendations(dbid = dbid,
                                                    begin_snap = begin_snap,
                                                    end_snap= end_snap)
            return data
        except Exception as ex:
            self._logger.error(f"Addm Process error. {ex}")            
        
            
