import os

import pytest
from utils.YamlUtil import YamlReader
from config.conf_dir import testdata_dir
print(testdata_dir + os.sep + "login.yaml")
test_data = YamlReader(testdata_dir + os.sep + "login.yaml").get_data()
print(test_data)


@pytest.mark.parametrize("data", test_data)
def test_login(data):
    print("111111", data)



