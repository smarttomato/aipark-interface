import os


root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_dir = os.path.join(root_path, "config" )

print(root_path, config_dir)