import pytest

@pytest.fixture
def login_model():
    return {
        "host": "some_host",
        "username": "some_username",
        "password": "some_password",
        "download_folder": "some_path"
    }
    