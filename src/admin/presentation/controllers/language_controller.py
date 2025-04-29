from admin.services.language_service import LanguageService
from admin.factory import AdminFactory
from logger import AppLogger

class LanguageController:
    
    _logger = AppLogger().get_logger()
    
    def __init__(self, admin_factory: AdminFactory):        
        self._service = LanguageService(admin_factory)

    def get_language(self):
        try:
            self._service.get_language()
        except Exception as ex:
            self._logger.error(f"Load language failed {ex}")
        