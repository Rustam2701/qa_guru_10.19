import requests
from .conftest import DOMAIN_URL


def test_successful_register():
    email = 'eve.holt@reqres.in'
    password = 'pistol'
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(url=DOMAIN_URL + '/register', json=payload)

    assert response.json()['id'] == 4
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'
    assert response.status_code == 200


def test_unsuccessful_register():
    email = "sydney@fife"
    payload = {
        'email': email,
    }
    response = requests.post(url=DOMAIN_URL + '/register', json=payload)

    assert response.json()['error'] == 'Missing password'
    assert response.status_code == 400
