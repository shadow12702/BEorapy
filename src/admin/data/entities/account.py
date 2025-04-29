# Description: Account

from datetime import datetime
from base.domain.base_entity import BaseEntity

class Account(BaseEntity):
    
    Username: str
    Email: str
    Password: str
    FailedLoginAttemps: int
    IsLocked: int
    CannotLoginUntilDate: datetime
    IsAdmin: int
    IsActived: int
    IsDeleted: int
    ActivationToken:str
    ActivationExpiry: int
    LastIpAddress: str
    CreateOn: datetime
    LastLoginDate: datetime
    LastActivityDate: datetime

    
    key_map = {
        **BaseEntity.key_map,
        "USERNAME"					    : "Username",
        "EMAIL"					        : "Email",
        "PASSWORD"                      : "Password",
        "FAILED_LOGIN_ATTEMPTS"			: "FailedLoginAttemps",
        "IS_LOCKED"                     : "IsLocked",
        "CANNOT_LOGIN_UNTIL_DATE_UTC"	: "CannotLoginUntilDate",
        "IS_ADMIN"                      : "IsAdmin",
        "ACTIVE"					    : "IsActived",
        "DELETED"					    : "IsDeleted",
        "ACTIVATION_TOKEN"              : "ActivationToken",
        "ACTIVATION_EXPIRY"             : "ActivationExpiry",
        "LAST_IP_ADDRESS"				: "LastIpAddress",
        "CREATED_ON_UTC"				: "CreateOn",
        "LAST_LOGIN_DATE_UTC"			: "LastLoginDate",
        "LAST_ACTIVITY_DATE_UTC"		: "LastActivityDate",
    }
    