import pytest
import requests


def test():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url=url)
    print(response)
