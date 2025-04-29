from admin.services.config_service import ConfigService
from core.config.config_manager import ConfigManager
from app.factory import ApplicationFactory
from admin.factory import AdminFactory
from data.oracle_db_context import OracleDbContext

# Khởi tạo db_context và app_factory
db_context = OracleDbContext()
app_factory = ApplicationFactory(db_context)
admin_factory = AdminFactory(db_context)

def get_app_factory():
    return app_factory

def get_admin_factory():
    return admin_factory

config_service = ConfigService(get_admin_factory())
config_manager = ConfigManager(config_service)
