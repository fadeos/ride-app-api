import pytest
from src.helper.util import get_ride_price


@pytest.fixture
def dataset():
    data_test =  {
    "distance": 4,
    "startTime": "2020-06-19T13:01:17.031Z",
    "duration": 3500
    }
    return data_test


def test_calculation(dataset):
    result = get_ride_price(dataset)
    
    assert result == 12.5