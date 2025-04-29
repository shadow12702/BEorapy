# Description: AccountService

import bcrypt
from datetime import datetime
from admin.data.model.account.login_model import LoginModel
from admin.factory import AdminFactory
from logger import AppLogger
from utils.email_sender import EmailSender
from dependencies import config_manager as cf_manager

class AccountService():
    _logger = AppLogger().get_logger()
    def __init__(self, factory: AdminFactory):
        self.account_repository = factory.account_repository()
    
    
    async def get_all(self):
        '''Get all accounts
        
        :return: list accounts'''
        return await self.account_repository.get_all()
    
    async def get_account(self, username:str):
        '''Get account by username
        
        :param username: account's username
        :return: account model'''
        return await self.account_repository.get_account(username=username)
    
    async def register(self, username: str, password: str, email:str=None):
        '''Register new account
        
        :param username: username use to login
        "param password: password of user
        :param email: email to active account
        :return: True when register successful else False
        '''
        try:
            account = await self.account_repository.get_account(username)
            if not account.is_empty:
                return False
            
            hash_pwd = self._hashPassword(password)                                
            activation_token = await self.account_repository.add(username=username, password=hash_pwd, email=email)
            
            if email and activation_token:
                return await self._sendActivationEmail(username, email, activation_token)
            return True
        except Exception as ex:
            self._logger.error(f"Register account failed. \n{ex}")            

    async def login(self, username: str, password: str, last_ip:str) -> LoginModel:
        '''Login to system
        '''
        try:
            account = await self.get_account(username)
            if not account.is_empty:
                if account.IsActived == 0 or account.IsDeleted == 1 or account.IsLocked > 0:
                    return LoginModel.empty()
                if not self._verify_password(password, account.Password):
                    failed_attempts = account.FailedLoginAttemps + 1
                    await self.account_repository.update_failed_attempts(username, failed_attempts, lock=1 if failed_attempts >= 5 else 0)
                    if account.Email:
                        await EmailSender.send_email(recipient=account.Email, subject="Orapy Account Locked", 
                                               body=cf_manager.mail_config.body.LockAccount.format(username))
                    return LoginModel.empty()
                else:
                    await self.account_repository.update_last_login(username, last_ip)
                    await self.account_repository.update_failed_attempts(username, 0)
                    return LoginModel(**{"USERNAME": account.Username, 
                                        "EMAIL": account.Email, 
                                        "IS_ADMIN": account.IsAdmin,
                                        "LAST_IP_ADDRESS":last_ip, 
                                        "LAST_LOGIN_DATE_UTC": datetime.utcnow()
                                        })
            return LoginModel.empty()
        except Exception as ex:
            self._logger.error(f"Login to system fail. \n{ex}")
            return LoginModel.empty()
        
    def _verify_password(self, password: str, hashed_password: str):
        return bcrypt.checkpw(password.encode(), hashed_password.encode())        
    
    async def _sendActivationEmail(self, username:str, email:str, activation_token: str):
        try:
            config = cf_manager.all_config
            activation_link = f"{config.http.url}/activate/{activation_token}"
            body = config.mail.body.activate.format(username, activation_link)
            await EmailSender.send_email(recipient=email, subject="Orapy Active Account", body = body)
            return True
        except Exception as ex:
            raise ex
        
    def _hashPassword(self, password:str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()        
    
    