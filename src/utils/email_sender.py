import asyncio
import smtplib
from email.mime.text import MIMEText
from logger import AppLogger
from dependencies import config_manager

class EmailSender():
    _logger = AppLogger().get_logger()
        
    @classmethod
    async def send_email(cls, recipient: str, subject:str, body:str):
        def sync_send_email():
            try:
                mail_cf = config_manager.mail_config.config
                msg = MIMEText(body, 'html')
                msg["From"] = mail_cf.Sender
                msg["Subject"] = subject
                msg["To"] = recipient
                
                if mail_cf.UseSsl:
                    with smtplib.SMTP_SSL(mail_cf.SmtpServer, mail_cf.SmtpPort) as server:
                        server.login(mail_cf.Sender, mail_cf.Password)
                        server.sendmail(mail_cf.Sender, recipient, msg.as_string())
                else:
                    with smtplib.SMTP(mail_cf.SmtpServer, mail_cf.SmtpPort) as server:
                        server.starttls()
                        server.login(mail_cf.Sender, mail_cf.Password)
                        server.sendmail(mail_cf.Sender, recipient, msg.as_string())
            except Exception as ex:
                cls._logger.error(f"sendEmail failed: \n{ex}")
        await asyncio.to_thread(sync_send_email)