import os

import allure
import requests
import pytest
from common.base import t_headers, t_data, t_host
from config.conf import config_dir


test_data = t_data(project="acb", file_name="login")
test_url = t_host(project="acb") + test_data[0]["path"]


@allure.feature("acb登录")
class TestAcbLogin:
    @pytest.mark.parametrize("data", test_data)
    def test_login(self, data):
        response = requests.post(url=test_url, data=data["data"], headers=t_headers()).json()

        desc = "<font color='#4287f5'>请求url: <font color='#000'>{} <br/>" \
               "<font color='#4287f5'>请求类型：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>期望结果：<font color='#000'>{} <br/>" \
               "<font color='#4287f5'>实际结果：<font color='#000'>{}".format(test_url, data["type"], data["expect"], response)
        allure.dynamic.title(data["case_name"])
        allure.dynamic.description_html(desc)

        # 保存sessionId
        if response["state"] == 0:
            with open(config_dir + os.sep + "session_id", "w") as f:
                f.write(response["value"]["sessionId"])

        assert response["state"] == data["expect"]["state"]


