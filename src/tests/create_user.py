"""tests for the creation of many users"""

import json

from printoptim import app


def test_create_user():
    tester = app.test_client()
    data_request = {"test": "nok"}
    response = tester.post('/create_user', data=data_request, content_type="application/json")
    assert response.status_code == 200
    assert json.loads(response.data) == {"test": "ok"}
