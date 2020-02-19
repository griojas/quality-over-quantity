from qoq import config_by_name

def test_config():
  assert 'test' in config_by_name

def test_app(client):
    response = client.get('/')

    assert b'<heading>Quality over Quantity</heading>' in response.data
    assert response.status_code == 200

def test_api_docs(client):
    response = client.get('/api', follow_redirects=True)
    assert b'<title>API</title>' in response.data
    assert response.status_code == 200

