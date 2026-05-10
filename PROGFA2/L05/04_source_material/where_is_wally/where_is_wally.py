import shutil
from pathlib import Path
from typing import List

my_path = Path('.')
def get_file(location : str):
    for path in Path(location).glob("*.txt"):
        path:Path

        with open(path, "r") as file:
            full_content = file.read()

        print(f"Wally is in {path}!")
        lines = full_content.split("\n")
        for index, line in enumerate(lines):
            if "Wally" in line:
                print(f"He's on line {index + 1}!")
        break

get_file(my_path)