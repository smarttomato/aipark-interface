import datetime
import os

# 目录配置
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_dir = os.path.join(root_path, "config")
common_dir = os.path.join(root_path, "common")
testdata_dir = os.path.join(root_path, "testdata")
testcase_dir = os.path.join(root_path, "testcase")
log_dir = os.path.join(root_path, "logs")
result_dir = os.path.join(root_path, "result")
report_dir = os.path.join(root_path, "report")

# 日志配置
log_info = {
    "log_level": "info",
    "log_file": os.path.join(log_dir, datetime.datetime.now().strftime("%Y-%m-%d") + ".log")
}
