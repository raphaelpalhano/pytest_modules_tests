from email import header
import json
import pytest
import requests


@pytest.mark.barriga_api
def test_barriga_api():
    # Arrange
    url = 'https://barrigarest.wcaquino.me/signin'
    body = {
        "email": "fake1@gmail.com","senha": "fake123","redirecionar": False
    }
    headerss = {'content-type': 'application/json'}

    # Act
    response = requests.post(url, data=json.dumps(body), headers=headerss)

    # assert
    assert response.status_code == 200 
