import allure
import requests
import pytest
import json
from configs.config import host
from common.base import get_test_data, get_headers, gms_data_combine


test_data = get_test_data("login", project="gms")
print(test_data)
# url = host["test"] + test_data[0]["path"]
url = host["gms"]["test"] + test_data[0]["path"]
print(url)

@allure.feature("GMS登录")
class TestLogin:
    @pytest.mark.parametrize("data", test_data)
    def test_login(self, data):
        print(gms_data_combine(data["data"]))
        response = requests.post(url=url, data=gms_data_combine(data["data"]), headers=get_headers()).json()

        desc = "<font color='#4287f5'>请求url: <font color='#000'>{} <br/>" \
               "<font color='#4287f5'>请求类型：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>期望结果：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>实际结果：<font color='#000'>{}".format(url, data["type"], data["expect"], response)
        # allure.dynamic.story(data["case_name"])
        allure.dynamic.title(data["case_name"])
        allure.dynamic.description_html(desc)
        print(response)
        assert response["success"]


if __name__ == '__main__':
    print(url)

