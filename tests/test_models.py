import pytest

from models import UpstreamLoginModel

def test_models(login_model):
    assert UpstreamLoginModel(**login_model)
