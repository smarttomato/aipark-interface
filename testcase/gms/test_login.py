import os

import allure
import requests
import pytest
from configs.config import host, testdata_dir
from common.base import get_test_data,  gms_data_combine, save_token


test_data = get_test_data("login", project="gms")
url = host["gms"]["test"] + test_data[0]["path"]


@allure.feature("GMS登录")
class TestLogin:
    @pytest.mark.parametrize("data", test_data)
    def test_login(self, data):
        response = requests.post(url=url, data=gms_data_combine(data["data"])).json()
        desc = "<font color='#4287f5'>请求url: <font color='#000'>{} <br/>" \
               "<font color='#4287f5'>请求类型：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>期望结果：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>实际结果：<font color='#000'>{}".format(url, data["type"], data["expect"], response)
        allure.dynamic.title(data["case_name"])
        allure.dynamic.description_html(desc)
        if response["success"]:
            save_token(response["data"]["token"], "gms")
        assert response["success"] == data["expect"]["success"]


if __name__ == '__main__':
    print(url)

