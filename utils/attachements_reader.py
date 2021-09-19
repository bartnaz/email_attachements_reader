import os
import datetime
import traceback

from imbox import Imbox

from . import AuthMixin, ServiceMixin


class EmailReader:
    def __init__(self):
        self.auth_data = None
        self.download_folder = None

    def get_attachements(self):

        self.auth_data = AuthMixin().get_auth_data()
        self.download_folder = self.auth_data.download_folder

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
        messages = mail.messages(date__gt=datetime.date(2018, 7, 30))

        for (uid, message) in messages:

            for idx, attachment in enumerate(message.attachments):
                try:
                    att_fn = attachment.get("filename")
                    download_path = f"{self.download_folder}/{att_fn}"
                    with open(download_path, "wb") as fp:
                        fp.write(attachment.get("content").read())
                except:
                    print(traceback.print_exc())

        mail.logout()
