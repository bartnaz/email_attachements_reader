import datetime
import os
import traceback

from imbox import Imbox

from . import AuthMixin, ServiceMixin


class EmailReader(ServiceMixin):
    def __init__(self):
        self.auth_data = None
        self.download_folder = None
        self.year_filter_variable = None
        self.month_filter_variable = None
        self.day_filter_variable = None

    def prepare_upstream_context(self):
        self.auth_data = AuthMixin().get_auth_data()
        self.download_folder = self.auth_data.download_folder
        self.remove_attachements_directory()
        self.specify_config_file()

    def get_attachements(self):
        try:
            self.prepare_upstream_context()

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

            specific_folder_list = [
                "INBOX",
                "INBOX.arrows",
                "INBOX.eden",
                "INBOX.ichp",
                "INBOX.inne",
                "INBOX.kielce",
                "INBOX.nazbud_ksiegowa",
                "INBOX.orange",
                "INBOX.print",
                "INBOX.tadex",
                "INBOX.upc",
            ]
            for folder in specific_folder_list:
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
