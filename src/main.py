import uvicorn
from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.presentation.route import *
from admin.presentation.route import *
from error_handler import error_handler
from logger import logger
from dependencies import get_app_factory, get_admin_factory, config_manager as cf_manager
from core.config.app_setting import app_setting


def register_admin_routes(app: FastAPI):
    """Dynamically register FastAPI routes based on config version."""
    version = cf_manager.app_config.Version  # Get the latest version
    default_routes = [route for route in app.router.routes if route.path in ["/openapi.json", "/docs", "/redoc"]]
    app.router.routes.clear()
    app.router.routes.extend(default_routes)

    # @app.get('/config', tags=["Default"], dependencies=[Depends(verify_auth)])
    # async def get_config():
    #     return cf_manager.all_config
    
    app.include_router(
        config_router, 
        prefix=f"/{version}/config",
        dependencies=[Depends(get_admin_factory)]
    )
    
    app.include_router(
        menu_router, 
        prefix=f"/{version}/menu",
        dependencies=[Depends(get_admin_factory)]
        )
    app.include_router(
        customer_router,
        prefix=f"/{version}/customer",
        dependencies=[Depends(get_admin_factory)]      
    )
    
def register_app_routes(app: FastAPI):
    """Dynamically register FastAPI routes based on config version."""
    version = cf_manager.app_config.Version  # Get the latest version
    
    app.include_router(
        auth_route, 
        prefix=f"/{version}/auth",
        dependencies=[Depends(get_app_factory)]
        )

    app.include_router(
        account_route,
        prefix=f"/{version}/account",
        dependencies=[Depends(get_app_factory)]
    )

    app.include_router(
        cdb_ash_overall_router,
        prefix=f"/{version}/cdb",
        dependencies=[Depends(get_app_factory)]
    )

    app.include_router(
        awr_repo_info_router,
        prefix=f"/{version}/awr",
        dependencies=[Depends(get_app_factory)]
    )
    
    app.include_router(
        patch_router,
         prefix=f"/{version}/patch",
        dependencies=[Depends(get_app_factory)]
    )
    
    app.include_router(
        best_practice_router,
         prefix=f"/{version}/best-practice",
        dependencies=[Depends(get_app_factory)]
    )


app = FastAPI(title="Loading...",
              description="Loading...",
              version= "Loading..."
              )

def update_app_metadata():
    _app_config = cf_manager.app_config
    app.title  = _app_config.Title
    app.description = _app_config.Description
    app.version = _app_config.Version
    
cf_manager.set_metadata_update_callback(update_app_metadata)
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    await cf_manager.load_config()
    register_admin_routes(app)    
    register_app_routes(app)
    yield
    logger.info("Application shutdown")
app.router.lifespan_context = lifespan



app.add_middleware(CORSMiddleware,
                   allow_origins=app_setting.config.cors.allow.origins,
                   allow_credentials = app_setting.config.cors.allow.credentials,
                   allow_methods = app_setting.config.cors.allow.methods,
                   allow_headers = app_setting.config.cors.allow.headers,
                   )

app.add_exception_handler(StarletteHTTPException, error_handler.http_exception_handler)
app.add_exception_handler(RequestValidationError, error_handler.validation_exception_handler)
app.add_exception_handler(Exception, error_handler.global_exception_handler)



if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)