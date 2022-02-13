import requests
import pytest
from common.base import Base


base = Base()
test_data = base.get_test_data("login")
url = base.get_url() + test_data[0]["url"]


@pytest.mark.parametrize("data", test_data)
def test_login(data):
    response = requests.post(url=url, data=data["data"]).json()
    print(response)
    assert response == data["expect"]


if __name__ == '__main__':
    print(url)

