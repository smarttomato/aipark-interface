from utils.YamlUtil import YamlReader
from configs.config import testdata_dir
import os

"""
一些公共方法
"""


def get_test_data(file_path):
    return YamlReader(testdata_dir + os.sep + file_path + ".yaml").get_data()


def headers():
    h = {
        "content-type": "application/json",
        "cookie": ""
    }
    return h


if __name__ == '__main__':

    print(get_test_data("login"))
