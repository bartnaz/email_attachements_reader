import datetime
import os
import traceback

from imbox import Imbox

from . import AuthMixin, ServiceMixin


class EmailReader(ServiceMixin):
    def __init__(self):
        self.auth_data = None
        self.download_folder = None
        self.folder_list = None
        self.year_filter_variable = None
        self.month_filter_variable = None
        self.day_filter_variable = None
        self.range = None

    def prepare_upstream_context(self, range: int):
        self.auth_data = AuthMixin().get_auth_data()
        self.download_folder = self.auth_data.download_folder
        self.folder_list = self.load_env_folders()
        self.remove_attachements_directory()
        self.get_month_from_range(range)

    def get_attachements(self, range: int):
        try:
            self.prepare_upstream_context(range)

            if not os.path.isdir(self.download_folder):
                os.makedirs(self.download_folder, exist_ok=True)

            mail = Imbox(
                self.auth_data.host,
                username=self.auth_data.username,
                password=self.auth_data.password,
                ssl=True,
                ssl_context=None,
                starttls=False,
            )

            for folder in self.folder_list:
                messages = None
                messages = mail.messages(
                    folder=folder,
                    date__gt=datetime.date(
                        self.year_filter_variable,
                        self.month_filter_variable,
                        self.day_filter_variable,
                    ),
                )

                for (uid, message) in messages:
                    for idx, attachment in enumerate(message.attachments):
                        try:
                            att_fn = attachment.get("filename")
                            att_fn = self.get_only_pdf_attachements(att_fn)
                            if att_fn != None:
                                self.save_attachements(attachment, att_fn)
                            else:
                                break
                        except:
                            print(traceback.print_exc())

            mail.logout()
        except:
            print(
                "An unexpected error occurred. Please check again your .env file in work directory"
            )
