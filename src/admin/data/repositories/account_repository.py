import secrets, time
from helper import helper
from logger import AppLogger
from data.db_context import DbContext, DataOperators
from admin.data.entities.account import Account
from typing import List

class AccountRepository():
    _logger = AppLogger().get_logger()
    
    def __init__(self, db_context: DbContext):
        if not isinstance(db_context, DataOperators):
            self._logger.error(TypeError("db_context must be a part of DataOperators"))
        self.db_context = db_context

    async def get_account(self, username:str) -> Account:
        '''Get Account info by Username

        :param code: configuration code
        :return: An Account model'''
        try:            
            query = """SELECT *
                       FROM SYS_ACCOUNT SA                         
                       WHERE USERNAME = :V_USERNAME"""
            account = await self.db_context.get_data(query, {'V_USERNAME': username})
            return Account(**account[0]) if len(account) > 0 else Account.empty()
        except Exception as ex:
            self._logger.error(f"getAccount error {ex}")


    async def get_all(self) -> List[Account]:
        '''Get all accounts

        :return: List of all accounts'''
        try:
            query = "SELECT * FROM SYS_ACCOUNT ORDER BY ID"
            data= await self.db_context.get_data(query)
            return [Account(**account) for account in data] if data else []
        except Exception as ex:
            self._logger.error(f"getAll error {ex}")

    

    async def add(self, username: str, password:str, email:str):
        '''Add account 

        :param username: username to login 
        :param password: password of user
        :param email: email of user to verify'''
        try:
            _activationExpiry = 84600
            query = """INSERT INTO SYS_ACCOUNT(USERNAME, EMAIL, PASSWORD, CANNOT_LOGIN_UNTIL_DATE_UTC, ACTIVE, DELETED, LAST_ACTIVITY_DATE_UTC, ACTIVATION_TOKEN, ACTIVATION_EXPIRY)
                       VALUES (:V_USERNAME, :V_EMAIL, :V_PASSWORD, 
                       TO_DATE(:V_CANNOT_LOGIN, 'DD/MM/YYYY HH24:MI:SS'),
                       :V_ACTIVE, :V_DELETED, 
                       TO_DATE(:V_LAST_ACTIVITY_DATE, 'DD/MM/YYYY HH24:MI:SS'), 
                       :V_ACTIVATION_TOKEN, :V_ACTIVATION_EXPIRY)
                       """
            activation_token = secrets.token_urlsafe(32)            
            await self.db_context.execute_query(query, {
                "V_USERNAME" : username,
                "V_EMAIL" : email if email else username+"@orapy.com",
                "V_PASSWORD" : password,
                "V_CANNOT_LOGIN": helper.get_date_utc(5), 
                "V_ACTIVE": 0 if email else 1,
                "V_DELETED": 0,
                "V_LAST_ACTIVITY_DATE": helper.get_date_utc(),
                "V_ACTIVATION_TOKEN" : activation_token if email else None,
                "V_ACTIVATION_EXPIRY" : int(time.time()) + _activationExpiry if email else None
                })
            return activation_token
        except Exception as ex:
            self._logger.error(f"Add an account error: \n{ex}")
    
    
    async def update_last_login(self, username:str, ip_address: str):
        '''Update last login 
        
        :param username: username
        :param ip_address: IP address         
        '''
        try:
            query = """UPDATE SYS_ACCOUNT
                        SET LAST_IP_ADDRESS = :V_LAST_IP,
                            LAST_LOGIN_DATE_UTC = TO_DATE(:V_LAST_LOGIN_DATE, 'DD/MM/YYYY HH24:MI:SS')
                       WHERE USERNAME = :V_USERNAME
                    """
            await self.db_context.execute_query(query, {
                "V_USERNAME" : username,
                "V_LAST_IP"  : ip_address,
                "V_LAST_LOGIN_DATE": helper.get_date_utc()
            })
            
        except Exception as ex:
            self._logger.error(f"updateLastLogin failed: \n{ex}")
            
    async def change_password(self, username: str, password: str):
        '''Change password of an account 

        :param username: username need to change password
        :param password: new password
        '''
        try:
            query = """UPDATE SYS_ACCOUNT
                       SET PASSWORD = :V_PASSWORD,
                           LAST_ACTIVITY_DATE_UTC = TO_DATE(:V_LAST_ACTIVITY, 'DD/MM/YYYY HH24:MI:SS')
                      WHERE USERNAME = :V_USERNAME"""
            await self.db_context.execute_query(query, {'V_USERNAME': username,
                                                 'V_PASSWORD': password,
                                                 "V_LAST_ACTIVITY": helper.get_date_utc()
                                                 })
        except Exception as ex:
            self._logger.error(f"change password error: \n{ex}")

    async def delete(self, id):
        '''Delete account

        :param id: Id of the account will be deleted'''
        try:
            query = """UPDATE SYS_ACCOUNT 
                        SET DELETED = 1, 
                            LAST_ACTIVITY_DATE_UTC = TO_DATE(:V_LAST_ACTIVITY, 'DD/MM/YYYY HH24:MI:SS')
                     WHERE ID = :V_ID"""
            return await self.db_context.execute_query(query, {'V_ID': id})
        except Exception as ex:
            self._logger.error(f"Delete account error: \nid: {id} \n{ex}")

    async def update_failed_attempts(self, username: str, failed_attempts:int, lock: int=0):
        '''Update failed attempt
        
        :param username: username login failed
        :param failed_attempts: failed count
        :param lock: lock account after failed count bigger than allow number
        '''
        try:
            query = """UPDATE SYS_ACCOUNT 
                        SET FAILED_LOGIN_ATTEMPTS = :V_FAILED_ATTEMPTS,
                            IS_LOCKED = :V_IS_LOCKED,
                            LAST_ACTIVITY_DATE_UTC = TO_DATE(:V_LAST_ACTIVITY, 'DD/MM/YYYY HH24:MI:SS')                            
                       WHERE USERNAME = :V_USERNAME"""
            return await self.db_context.execute_query(query, {
                'V_USERNAME': username,
                'V_FAILED_ATTEMPTS': failed_attempts,
                'V_IS_LOCKED': lock,
                'V_LAST_ACTIVITY': helper.get_date_utc()
                })
        except Exception as ex:
            self._logger.error(f"Update failed attempts error: \n{ex}")
            
    