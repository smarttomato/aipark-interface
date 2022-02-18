import allure
import requests
import pytest
from common.base import Base


base = Base()
test_data = base.get_test_data("login")
url = base.get_url() + test_data[0]["url"]


class Test_Login:
    @pytest.mark.parametrize("data", test_data)
    @allure.title("测试登录")
    def test_login(self, data):
        allure.dynamic.title( data["case_name"])
        response = requests.post(url=url, data=data["data"]).json()
        print(response)
        assert response == data["expect"]


if __name__ == '__main__':
    print(url)

