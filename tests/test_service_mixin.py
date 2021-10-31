import pytest
import freezegun
from dotenv import load_dotenv

from utils import ServiceMixin

def test_load_env_folders():
    load_dotenv()
    folders_list = ServiceMixin.load_env_folders()
    assert folders_list == ["INBOX", "INBOX.arrows", "INBOX.eden", "INBOX.ichp", "INBOX.inne", "INBOX.kielce", "INBOX.nazbud_ksiegowa", "INBOX.orange", "INBOX.print", "INBOX.tadex", "INBOX.upc"]
    
@freezegun.freeze_time("19.01.2021")
def test_get_current_date():
    assert ServiceMixin._get_current_date() == (1, 2021)

@freezegun.freeze_time("19.01.2021")
@pytest.mark.parametrize("date_range, expected_month", [("1", "12"), ("2", "11"), ("3", "10")])
def test_get_month_from_range(date_range, expected_month):
        return_date_tuple = ServiceMixin().get_month_from_range(int(date_range))
        assert return_date_tuple == (2021, int(expected_month), 1)

@freezegun.freeze_time("19.02.2021")
@pytest.mark.parametrize("date_range, expected_month", [("1", "1"), ("2", "12"), ("3", "11")])
def test_get_month_from_range_febr(date_range, expected_month):
        return_date_tuple = ServiceMixin().get_month_from_range(int(date_range))
        assert return_date_tuple == (2021, int(expected_month), 1)

@pytest.mark.parametrize("current_month, date_range", [("1", "1")])
def test_get_real_month(current_month, date_range):
    return_date = ServiceMixin()._get_real_month(int(current_month), int(date_range))
    assert return_date == 12
