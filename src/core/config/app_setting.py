# Description: Application config 

import json
import os
from watchdog.observers import Observer
from base.model.mapped_base_model import MappedBaseModel
from core.config.config_loader import ConfigChangeHandler
from core.enum.app_enum import AppEnum
from helper import helper

class AppSetting:
    '''CORS settings'''
    _instance = None
        
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(AppSetting, cls).__new__(cls)
            cls._instance._load()
            cls._instance._json_hot_reload()
        return cls._instance
        
    def _load(self):
        '''CORS loading '''
        with open(AppEnum.JSON_CONFIG.file_path, "r") as js_file:
            config_json = json.load(js_file)
        
        self.config = self._load_json(config_json)
        
    def _load_json(self, js_config):
        js_data = helper.to_nested_dict({k: helper.to_nested_dict(v) if isinstance(v, dict) else v 
                                                for k, v in js_config.items()})
        return MappedBaseModel(**js_data)
        
    def _json_hot_reload(self):
        '''Set up hot-reload when config.json has been changed'''
        event_handler = ConfigChangeHandler(self, AppEnum.JSON_CONFIG.file_path)
        observer = Observer()
        observer.schedule(event_handler, 
                          path= os.path.dirname(AppEnum.JSON_CONFIG.file_path),
                          recursive=False)


app_setting = AppSetting()