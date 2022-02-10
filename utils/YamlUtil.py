import yaml
import os
import json
from config.conf_dir import config_dir, common_dir


class YamlReader:

    def __init__(self, yaml_file):
        if os.path.exists(yaml_file):
            self.yaml_file = yaml_file
        else:
            raise FileNotFoundError("文件不存在")

    def get_data(self):
        with open(self.yaml_file, "rb") as f:
            r = yaml.safe_load(f)
            return r

    def save_data(self, data):
        with open(self.yaml_file, "w") as f:
            yaml.dump(data, f)


if __name__ == '__main__':
    pass