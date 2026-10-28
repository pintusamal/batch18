import json
import os
from pathlib import Path


def get_project_root():
    current_file = Path(__file__)  # common funtion.py
    return current_file.parent.parent

def read_json_data(key):
    project_root = get_project_root()
    json_path  = project_root / "data" / "input_data.json"
    with open(json_path , "r") as json_file:
        data = json.load(json_file)
        return data[key]

