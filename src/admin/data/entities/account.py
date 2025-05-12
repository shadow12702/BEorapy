# Description: Account

from datetime import datetime
from base.domain.base_entity import BaseEntity

class Account(BaseEntity):
    
    username: str
    email: str
    password: str
    failed_login_attemps: int
    is_locked: int
    cannot_login_until_date: datetime
    is_admin: int
    is_actived: int
    is_deleted: int
    activation_token:str
    activation_expiry: int
    last_ip_address: str
    create_at: datetime
    last_login_date: datetime
    last_activity_date: datetime

    
    key_map = {
        **BaseEntity.key_map,
        "USERNAME"					    : "username",
        "EMAIL"					        : "email",
        "PASSWORD"                      : "password",
        "FAILED_LOGIN_ATTEMPTS"			: "failed_login_attemps",
        "IS_LOCKED"                     : "is_locked",
        "CANNOT_LOGIN_UNTIL_DATE_UTC"	: "cannot_login_until_date",
        "IS_ADMIN"                      : "is_admin",
        "ACTIVE"					    : "is_actived",
        "DELETED"					    : "is_deleted",
        "ACTIVATION_TOKEN"              : "activation_token",
        "ACTIVATION_EXPIRY"             : "activation_expiry",
        "LAST_IP_ADDRESS"				: "last_ip_address",
        "CREATED_ON_UTC"				: "create_at",
        "LAST_LOGIN_DATE_UTC"			: "last_login_date",
        "LAST_ACTIVITY_DATE_UTC"		: "last_activity_date",
    }
    