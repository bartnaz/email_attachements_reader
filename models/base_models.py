from pydantic import BaseModel

class UpstreamLoginModel(BaseModel):
    host: str
    username: str
    password: str
    download_folder: str