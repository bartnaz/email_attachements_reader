import datetime
import os

from dotenv import load_dotenv
from models import UpstreamLoginModel
from .consts import MONTH_FEBRUARY_MAP, MONTH_JANUARY_MAP, MONTH_MARCH_MAP

FILE_TYPE_MAP = {
    "pdf": "pdf",
    "PDF": "PDF",
    "7z": "7z",
    "zip": "zip",
    "rar": "rar",
}


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
    def save_attachements(self, attachment, att_fn):
        download_path = f"{self.download_folder}/{att_fn}"
        if os.path.exists(download_path):
            download_path = f"{self.download_folder}/{att_fn}(1)"
        with open(download_path, "wb") as fp:
            fp.write(attachment.get("content").read())

    def get_only_pdf_attachements(self, att_name: str):
        name_check = att_name.split(".")
        if FILE_TYPE_MAP.get(name_check[-1], None) != None:
            return att_name

    def remove_attachements_directory(self):
        if os.path.isdir(self.download_folder):
            files_in_dir = os.listdir(self.download_folder)
            for file in files_in_dir:
                os.remove(f"{self.download_folder}/{file}")
            os.removedirs(self.download_folder)

    def get_month_from_range(self, range):
        current_month, current_year = self._get_current_date()
        self.year_filter_variable = current_year
        self.month_filter_variable = self._get_real_month(current_month, range)
        self.day_filter_variable = 1
        return (
            self.year_filter_variable,
            self.month_filter_variable,
            self.day_filter_variable,
        )
    
    @staticmethod
    def load_env_folders():
        folder_list = os.getenv("SPECIFIC_FOLDER_LIST")
        return folder_list.split(", ")

    @staticmethod
    def _get_real_month(current_month, range):
        if current_month < 4:
            if current_month == 3:
                current_month = MONTH_MARCH_MAP.get(range)
                return current_month
            elif current_month == 2:
                current_month = MONTH_FEBRUARY_MAP.get(range)
                return current_month
            elif current_month == 1:
                current_month = MONTH_JANUARY_MAP.get(range)
                return current_month
            diff = current_month - range
            current_month = 12 - abs(diff)
            return current_month
        current_month = current_month - range
        return current_month

    @staticmethod
    def _get_current_date():
        current_date = datetime.date.today()
        return int(current_date.strftime("%m")), int(current_date.strftime("%Y"))

    @staticmethod
    def _prepare_data_from_string(data):
        split_data = data.split("-")
        int_data = []
        for item in split_data:
            item = int(item)
            int_data.append(item)
        return int_data
