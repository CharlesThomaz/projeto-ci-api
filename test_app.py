import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'API conectada ao MySQL' in response.data

def test_get_items(client):
    response = client.get('/items')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_post_item(client):
    item = {'name': 'Item de Teste'}
    response = client.post('/items', data=json.dumps(item), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == 'Item adicionado com sucesso'
