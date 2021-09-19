import os
import datetime

from dotenv import load_dotenv

from models import UpstreamLoginModel


class AuthMixin:
    def __init__(self):
        load_dotenv()
        self.host = f"{os.getenv('HOST')}"
        self.username = f"{os.getenv('MAIL_USERNAME')}"
        self.password = f"{os.getenv('PASSWORD')}"
        self.download_folder = f"{os.getenv('DOWNLOAD_FOLDER')}"

    def get_auth_data(self):
        return UpstreamLoginModel(
            host=self.host,
            username=self.username,
            password=self.password,
            download_folder=self.download_folder,
        )


class ServiceMixin:
    @staticmethod
    def get_current_month_mail_filter():
        return datetime.date.today().year, datetime.date.today().month, 1
