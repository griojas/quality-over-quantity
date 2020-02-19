
import os
import json

from datetime import datetime, date, timedelta


def test_api_stats_missing_all_tokens(client):

    headers = {
      'Content-Type': 'application/json'
    }

    response = client.post('/api/stats', headers=headers)

    assert response.status_code == 400
    assert response.get_json()['message'] == 'Missing VCS/CI token from payload'
    

def test_api_stats_missing_ci_token(client):
    headers = {
      'Content-Type': 'application/json'
    }

    data = {
      'vcs_token': 'dummytoken'
    }

    response = client.post('/api/stats', data=data, headers=headers)

    assert response.status_code == 400
    assert response.get_json()['message'] == 'Missing VCS/CI token from payload'

def test_api_stats_valid_tokens(client):
    headers = {
      'Content-Type': 'application/json'
    }

    assert 'VCS_TOKEN' in os.environ, "VCS_TOKEN environment variable must be set"
    assert 'CI_TOKEN' in os.environ, "CI_TOKEN environment variable must be set"
    
    data = {
      'vcs_token': os.environ['VCS_TOKEN'],
      'ci_token': os.environ['CI_TOKEN']
    }

    response = client.post('/api/stats', data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    assert response.get_json()
    