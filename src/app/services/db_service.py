# Description: 

from abc import ABC, abstractmethod
import pandas as pd

class DbService(ABC):
    
    @property
    @abstractmethod
    def repository(self):
        '''Repository to be provided by subclass'''
        pass
    
    @property
    @abstractmethod
    def multiThreads(self):
        '''Repository to be provided by subclass'''
        pass
    
    @property
    @abstractmethod
    def CSV_OUTPUT_PATH(self) -> str:
        '''CSV Output path to be provided by subclass'''
        pass
    
    
    def processing(self, functions):
        
        def result_callback(fn_name, result):
            try:
                data = [res.__dict__ for res in result if res is not None]                
                pd.DataFrame(data).to_csv(f"{self.CSV_OUTPUT_PATH}/{fn_name}.csv", index=False)
            except Exception as ex:
                raise ex
        
        try:
            tasks = [
                (getattr(self.repository, fn_name), args, kwargs)
                for fn_name, args, kwargs in functions                
            ]            
            self.multiThreads.execute(tasks, callback=result_callback)
        except Exception as ex:
            raise ex
