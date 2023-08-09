"""Helper function for import and export data"""
import os
import pickle
import json
from typing import Any


def export_object(filename: str,
                  obj: Any,
                  path: str = "./result/"
                  ) -> None:
    file = os.path.join(path, filename)
    with open(file + ".pickle", "w+b") as f:
        pickle.dump(obj, f)


def json_to_obj(filename: str) -> Any:
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.loads(json_file.read())

