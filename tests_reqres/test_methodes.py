import requests
from .conftest import USER_URL


def test_get_users():
    response = requests.get(url=USER_URL, params={'page': 2})

    assert response.json()['page'] == 2


def test_create_user():
    name = 'Jhon'
    job = 'Teacher'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.post(url=USER_URL, json=payload)

    assert response.json()['job'] == job
    assert response.json()['name'] == name
    assert response.status_code == 201


def test_update_user():
    name = 'morpheus'
    job = 'zion resident'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.put(url=USER_URL + '/2', json=payload)

    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_delete_user():
    response = requests.delete(url=USER_URL + '/2')

    assert response.text == ''
    assert response.status_code == 204
