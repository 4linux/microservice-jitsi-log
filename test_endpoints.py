import pytest

from flaskr import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_healthcheck(client):
    r = client.get('/healthcheck')
    print(r.get_json()) 
