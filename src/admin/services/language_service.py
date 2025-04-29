from logger import AppLogger
from admin.factory import AdminFactory

class LanguageService():

    _logger = AppLogger().get_logger()
    
    def __init__(self, repo_factory: AdminFactory, language:str='en'):
        self.languageCode = language
        self.languageRepo = repo_factory.languageRepository(language)

    def getLanguages(self):
        return self.languageRepo.getAll()
        
    