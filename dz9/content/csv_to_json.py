import json
from pathlib import Path
from typing import Callable
OUT = Path("answers.json")


def json_converter(file: Path = OUT):

    def j_c_deco(func: Callable):
        nonlocal file
        def wrapper(*args, **kwargs):
            temp = func(args[0])
            with open(file=file,mode="wt",encoding="utf-8") as j_o:
                json.dump(temp,j_o,indent=1)
            return True

        return wrapper
    return j_c_deco
