import random
import shutil
from pathlib import Path
from typing import List

my_path = Path(r".")
python = my_path /  r"PYTHON"

# print(path.stem)

for path in Path(python).rglob("*"):
    # print(f"=== THE {path.parent} SPIRITS HAVE SPOKEN! ===")
    with open(path, "r") as file:
        content = file.read()

    line = content.split("\n")
    for line in file:
        random_line = random.choice(line)
        print(random_line)
        break
