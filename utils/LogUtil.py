import logging
from configs.config import log_info

# 定义日志级别
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


class Logger:

    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level

        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(log_l[self.log_level])
        if not self.logger.handlers:
            # 输出控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s ')
            fh_stream.setFormatter(formatter)
            # 写入文件
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)
            # 添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


# 供外部使用
def set_log(log_name=__file__):
    return Logger(log_file=log_info["log_file"], log_name=log_name, log_level=log_info["log_level"]).logger


if __name__ == "__main__":
    set_log().error("this is a error")
