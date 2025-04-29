import threading
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHttpException
from logger import AppLogger

class ErrorHandler:
    _instance = None
    _lock = threading.Lock()
    _logger = AppLogger().get_logger()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(ErrorHandler, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    async def http_exception_handler(self, _: Request, exc: StarletteHttpException):
        '''Http Exception'''
        self._logger.error(f"HttpException: {exc.detail}")
        return JSONResponse(status_code=exc.status_code,
                            content={"detail": exc.detail})
    
    async def validation_exception_handler(self, _: Request, exc: RequestValidationError):
        '''Validation exception'''
        self._logger.error(f"Validation Error: {exc.errors()}")
        return JSONResponse(status_code=442, 
                            content={"detail": exc.errors() })
        
    async def global_exception_handler(self, _: Request, exc: Exception):
        '''Exception Handler 
        '''
        self._logger.exception(f"Unhandled Exception: {str(exc)}")
        return JSONResponse(status_code=500,
                            content={"detail":"Internal Server Error"})
        
error_handler = ErrorHandler()
