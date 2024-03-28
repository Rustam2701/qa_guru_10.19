import requests
from .conftest import USER_URL, DOMAIN_URL


def test_get_user():
    response = requests.get(USER_URL + '/2')

    assert response.status_code == 200


def test_not_found_user():
    response = requests.get(USER_URL + '/23')

    assert response.json() == {}
    assert response.status_code == 404


def test_not_validate_user():
    response = requests.post(DOMAIN_URL + '/register')

    assert response.status_code == 400
