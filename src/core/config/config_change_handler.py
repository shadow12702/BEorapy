# Description: ConfigChangeHandler

from watchdog.events import FileSystemEventHandler

class ConfigChangeHandler(FileSystemEventHandler):
    """Reload config when file INI changed"""
    def __init__(self, class_setting, cf_file: str):
        self._setting = class_setting
        self.config_file = cf_file

    def on_modified(self, event):
        if event.src_path == self.config_file:
            print("Detected change in config file. Reloading...")
            self._setting._load_config()
