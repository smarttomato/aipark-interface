import hashlib
import os
from utils.YamlUtil import YamlReader
from config.conf import config_dir, testdata_dir


"""
一些公共方法
"""


def t_headers(content_type="application/x-www-form-urlencoded;charset=UTF-8"):
    with open(config_dir + os.sep + "session_id", "r") as f:
        s_id = f.read()
    return {
        "content-type": content_type,
        "Session-Id": s_id
    }


def t_data(project, file_name, page=None):
    if page:
        return YamlReader(testdata_dir + os.sep + project + os.sep + page + os.sep + file_name + ".yaml").get_data()
    else:
        return YamlReader(testdata_dir + os.sep + project + os.sep + file_name + ".yaml").get_data()


def t_host(project, env="test"):
    return YamlReader(config_dir + os.sep + "host.yaml").get_data()[env]["url"][project]


# md5加密
def do_md5(str_input):
    new_str = str_input.encode()
    m = hashlib.md5()
    m.update(new_str)
    return m.hexdigest()


if __name__ == '__main__':
    t_data(project="acb", file_name="login")

