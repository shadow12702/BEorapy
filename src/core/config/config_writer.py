# Description:

import configparser
from core.enum.app_enum import AppEnum


class ConfigWriter:
    '''Write config to file'''
    @staticmethod
    def write(section: str = "DEFAULT", **kwargs):
        '''Write config to file'''
        config = configparser.ConfigParser()
        config.read(AppEnum.APP_CONFIG_FILE.file_path)
        if not config.has_section(section):
            config.add_section(section)
        [config.set(section, key, str(value)) for key, value in kwargs.items()]
        with open(AppEnum.APP_CONFIG_FILE.file_path, 'w') as cf_file:
            config.write(cf_file)
