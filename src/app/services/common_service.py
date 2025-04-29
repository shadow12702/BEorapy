# Description: 

from app.factory import ApplicationFactory
from app.data.entities.checkdb import CheckDb
from app.data.entities.db_version import DbVersion
from typing import List


class CommonService():
    
    
    def __init__(self, app_factory: ApplicationFactory):
        # 
        self.repository = app_factory.common_repository()        

    @property
    def db_version(self) -> DbVersion:
        '''Get version of current database
        
        Return: 
            Version number'''
        return self.repository.get_db_version()        

    @property
    def db_open_mode(self) -> str:
        '''Get Open Mode of database
        
        Return: 
            Open Mode status'''
        return self.repository.getDbOpenMode()        

    def checkDbStatus(self, db_name:str)-> List[CheckDb] :
        '''Checking status of database. If connect successfully then return list of CheckBb
        
        Args:
            db_name: database name want to check status
        
        Return: 
            A List[CheckDb]
        '''        
        return self.repository.checkDbStatus(db_name)
        
    def getDbName(self, dbid):
        '''Get Database Name by dbid
        
        Args:
            dbid: DBID number
        
        Return: 
            Database name
        '''
        return self.repository.getDbName(dbid=dbid)
    
