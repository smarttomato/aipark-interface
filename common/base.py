import hashlib
from utils.YamlUtil import YamlReader
from configs.config import testdata_dir
import os

"""
一些公共方法
"""


def get_test_data(file_path):
    return YamlReader(testdata_dir + os.sep + file_path + ".yaml").get_data()


def get_headers():
    headers = {
        "content-type": "application/json",
        "cookie": ""
    }
    return headers


def do_md5(str_input):
    new_str = str_input.encode()
    m = hashlib.md5()
    m.update(new_str)
    return m.hexdigest()


if __name__ == '__main__':
    print(do_md5("1"))
    print(get_test_data("login"))
