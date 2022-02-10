import os


root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_dir = os.path.join(root_path, "config")
common_dir = os.path.join(root_path, "common")
testdata_dir = os.path.join(root_path, "testdata")



print(root_path, config_dir, common_dir)