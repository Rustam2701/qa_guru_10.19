import requests
from .conftest import USER_URL, DOMAIN_URL


def test_with_answer():
    response = requests.get(url=DOMAIN_URL + '/unknown')

    assert response.json()["page"] == 1
    assert response.status_code == 200


def test_without_answer():
    response = requests.get(url=USER_URL + '/unknown/2')

    assert response.json() == {}
    assert response.status_code == 404
