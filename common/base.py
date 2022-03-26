import hashlib
from utils.YamlUtil import YamlReader
from configs.config import testdata_dir
import os
import time

"""
一些公共方法
"""


def get_gms_urlsign(params, timestamp):
    s = ""
    # timestamp = str(int(time.time()))
    secret = "Fr2rsAJYtqlofdhkhiNuTqMoU8sFCdMF"
    appkey = "6800548364"
    pre_str = "appkey={}&timestamp={}".format(appkey, timestamp)

    # 拼接参数
    for d in params:
        pre_str = pre_str + "&" + d + "=" + params[d]
    # 排序后再拼接secret
    param_list = pre_str.split("&")
    param_list.sort()
    for i in param_list:
        s = s + i + "&"
    s = s + "secret=" + do_md5(secret).upper()
    # 返回加密后的urlsign
    print(do_md5(s).upper())
    return do_md5(s).upper()


def get_test_data(file_path, project=""):
    return YamlReader(testdata_dir + os.sep + project + os.sep + file_path + ".yaml").get_data()


def gms_data_combine(params):
    timestamp = str(int(time.time()))
    params["urlsign"] = get_gms_urlsign(params, timestamp)
    params["timestamp"] = timestamp
    params["appkey"] = "6800548364"
    return params


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
    # print(do_md5("1"))
    d = {'passport': 'zhangzhimeng', 'password': 'Aa123123', 'namespace': 'gms'}
    get_gms_urlsign(d, timestamp="1648291469")
    get_test_data("login", project="gms")
