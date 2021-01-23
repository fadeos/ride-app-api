import falcon
from falcon import testing
import pytest
from src.data.data import DATA_RIDES

from app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_list_rides_api(client):
    
    response = client.simulate_get('/v1/rides')
    
    assert response.json == DATA_RIDES
    assert response.status == falcon.HTTP_OK


def test_calculation_api(client):
    
    response = client.simulate_get('/v1/calculation?id=1')
    
    assert response.json['price'] == 7.5
    assert response.status == falcon.HTTP_OK