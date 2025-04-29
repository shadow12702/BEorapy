from enum import Enum
from pathlib import Path

ROOT_AT = 'src'
class AppEnum(Enum):
    
    # Config file
    APP_CONFIG_FILE = 'config/application.ini'
    JSON_CONFIG = 'config/config.json'
    
    # Data file
    SQL_CONFIGURATION_FILE = '../data/sql_config.json'
    BEST_PRACTICE_19C = '../data/best_practice_19c.csv'
    LIST_PATCHES_19C = '../data/patches.csv'
    
    @property
    def file_path(self):
        current_path = Path(__file__).parent
        index = current_path.parts.index(ROOT_AT)
        base_path = Path(*current_path.parts[:index+1])
        path = (base_path/self.value).resolve()
        return path
        
    