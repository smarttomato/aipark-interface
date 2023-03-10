import os

import pytest
from config.conf import report_dir, result_dir
import time
import subprocess

current_time = time.strftime('%Y-%m-%d-%H-%M-%S')
result_name = result_dir + '{}interface_autotest_{}'.format(os.sep, current_time)
report_name = report_dir + "{}allure_report_{}".format(os.sep, current_time)
pytest.main([
             '-s', '-q',
             '-p', 'no:warnings',
             # '--reruns', '2',
             '--alluredir', result_name,
            ])

print("allure generate {} -o {}".format(result_name, report_name))
subprocess.call("allure generate {} -o {}".format(result_name, report_name), shell=True)
