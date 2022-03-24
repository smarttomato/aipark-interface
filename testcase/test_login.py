import allure
import requests
import pytest
import json
from configs.config import host
from common.base import get_test_data, get_headers


test_data = get_test_data("login")
# url = host["test"] + test_data[0]["path"]
url = host["dev"] + test_data[0]["path"]


@allure.feature("登录接口")
class TestLogin:
    @pytest.mark.parametrize("data", test_data)
    def test_login(self, data):
        response = requests.post(url=url, data=json.dumps(data["data"]), headers=get_headers()).json()

        desc = "<font color='#4287f5'>请求url: <font color='#000'>{} <br/>" \
               "<font color='#4287f5'>请求类型：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>期望结果：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>实际结果：<font color='#000'>{}".format(url, data["type"], data["expect"], response)
        # allure.dynamic.story(data["case_name"])
        allure.dynamic.title(data["case_name"])
        allure.dynamic.description_html(desc)
        assert response["status"] == data["expect"]["status"]


if __name__ == '__main__':
    print(url)

