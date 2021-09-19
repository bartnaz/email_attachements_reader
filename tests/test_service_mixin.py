import pytest
import freezegun

from utils import ServiceMixin


@freezegun.freeze_time("19.09.2021")
def test_get_current_month_mail_filter():
    expected_value = ServiceMixin.get_current_month_mail_filter()
    assert expected_value == (2021, 9, 1)
