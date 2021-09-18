import os
import datetime

from dotenv import load_dotenv


class ServiceMixin():
    @staticmethod
    def get_auth():
        load_dotenv()

        return {
            "HOST": f"{os.getenv('HOST')}",
            "USERNAME": f"{os.getenv('MAIL_USERNAME')}",
            "PASSWORD": f"{os.getenv('PASSWORD')}",
            "DOWNLOAD_FOLDER": f"{os.getenv('DOWNLOAD_FOLDER')}",
        }
    
    @staticmethod
    def get_current_month_mail_filter():
        return datetime.date.today().year, datetime.date.today().month, 1