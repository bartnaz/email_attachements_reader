import os

from dotenv import load_dotenv
from models import UpstreamLoginModel
from .consts import FILE_TYPE_MAP


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
                os.remove(f"{self.download_folder}\{file}")
            os.removedirs(self.download_folder)

    def specify_config_file(self):
        load_dotenv()
        date_input = f"{os.getenv('LOAD_DATA_FROM')}"
        (
            self.year_filter_variable,
            self.month_filter_variable,
            self.day_filter_variable,
        ) = self._prepare_data_from_string(date_input)

    @staticmethod
    def _prepare_data_from_string(data):
        split_data = data.split("-")
        int_data = []
        for item in split_data:
            item = int(item)
            int_data.append(item)
        return int_data
