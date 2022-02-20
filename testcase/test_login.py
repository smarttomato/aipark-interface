import allure
import requests
import pytest
from configs.config import host
from common.base import get_test_data


test_data = get_test_data("login")
url = host["test"] + test_data[0]["path"]


@allure.feature("登录接口")
class TestLogin:
    @pytest.mark.parametrize("data", test_data)
    def test_login(self, data):
        response = requests.post(url=url, data=data["data"]).json()
        desc = "<font color='#4287f5'>请求url: <font color='#000'>{} <br/>" \
               "<font color='#4287f5'>请求类型：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>期望结果：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>实际结果：<font color='#000'>{}".format(url, data["type"], data["expect"], response)
        # allure.dynamic.story(data["case_name"])
        allure.dynamic.title(data["case_name"])
        allure.dynamic.description(desc)
        assert response == data["expect"]


if __name__ == '__main__':
    print(url)

