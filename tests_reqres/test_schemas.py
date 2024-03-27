import requests
from jsonschema import validate

from schemas.get_list_resource import GetListResource
from schemas.get_list_users import GetUsers
from schemas.get_single_resource import GetSingleResource
from schemas.get_single_user import GetSingleUser
from .conftest import USER_URL, DOMAIN_URL


def test_get_list_resource_validation():
    response = requests.get(url=DOMAIN_URL + '/unknown')
    validate(response.json(), GetListResource)


def test_get_list_users_validation():
    response = requests.get(url=USER_URL, params={"page": 2})
    validate(response.json(), GetUsers)


def test_get_single_resource_validation():
    response = requests.get(url=DOMAIN_URL + '/unknown/2')
    validate(response.json(), GetSingleResource)


def test_get_single_user_validation():
    response = requests.get(url=USER_URL + '/2')
    validate(response.json(), GetSingleUser)
