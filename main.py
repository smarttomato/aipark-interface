import pytest
from configs.config import report_dir
import time

current_time = time.strftime('%Y-%m-%d %H-%M-%S')

pytest.main([
             '-s', '-q',
             '-p', 'no:warnings',
             # '--reruns','1',
             '--alluredir', report_dir + '/interface_autotest_{0}'.format(current_time),
            ])
