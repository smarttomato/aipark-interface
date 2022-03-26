import hashlib
from utils.YamlUtil import YamlReader
from configs.config import testdata_dir
import os
import time

"""
一些公共方法
"""

appkey = "6800548364"


# 获取gms的urlsign
def get_gms_urlsign(params, timestamp):
    s = ""
    secret = "Fr2rsAJYtqlofdhkhiNuTqMoU8sFCdMF"
    pre_str = "appkey={}&timestamp={}".format(appkey, timestamp)

    # 拼接参数
    for p in params:
        pre_str = pre_str + "&" + p + "=" + params[p]
    # 排序后再拼接secret
    param_list = pre_str.split("&")
    param_list.sort()
    for i in param_list:
        s = s + i + "&"
    s = s + "secret=" + do_md5(secret).upper()
    return do_md5(s).upper()


def save_token(token, project):
    with open(testdata_dir + os.sep + project + os.sep + "token", "w") as f:
        f.write(token)


# 获取yaml测试data
def get_test_data(file_path, project=""):
    return YamlReader(testdata_dir + os.sep + project + os.sep + file_path + ".yaml").get_data()


# 测试data添加urlsign，timestamp，appkey
def gms_data_combine(params):
    timestamp = str(int(time.time()))
    params["urlsign"] = get_gms_urlsign(params, timestamp)
    params["timestamp"] = timestamp
    params["appkey"] = appkey
    return params


def get_headers(content_type="application/json"):
    headers = {
        "content-type": content_type,
        "cookie": ""
    }
    return headers


# md5加密
def do_md5(str_input):
    new_str = str_input.encode()
    m = hashlib.md5()
    m.update(new_str)
    return m.hexdigest()


if __name__ == '__main__':
    # print(do_md5("1"))
    test_data = {'username': 'zhangzhimeng', 'password': 'Aa123123', 'namespace': 'gms'}
    get_gms_urlsign(test_data, timestamp="1648299940")
    gms_data_combine(test_data)
