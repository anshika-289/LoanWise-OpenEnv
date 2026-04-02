import json
from pathlib import Path


def load_applications():
    data_path = Path("data/applications.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)