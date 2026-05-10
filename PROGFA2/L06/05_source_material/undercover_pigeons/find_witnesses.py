# The Great Pigeon Witness Protection Program
import random
import shutil
from pathlib import Path
from typing import  List
import csv

from pigeon import Pigeon

path = "witnesses"
path = "witnesses_obfuscated"

for path in Path(path).rglob("*.csv"):
    print(path.stem)
    with path.open("r") as file:
        reader = csv.DictReader(file)
        # print(reader.fieldnames)

        for pigeon_row in reader:
            try:
                name = pigeon_row["Pigeon Name"]
                identity = pigeon_row["New Identity"]
                relocation = pigeon_row["Relocation City"]
                favorite_snack = pigeon_row["Favorite Snack"]
                security_level = pigeon_row["Security Level (1-5)"]

                pigeons = Pigeon(name, identity, favorite_snack, security_level)
                print(pigeons)
            except KeyError as error:
                print(f"[ERROR] error in csv, assumed incorrect witness file: {pigeon_row}")
            except ValueError as error:
                print(f"[ERROR] -> value errors in line: {pigeon_row}")
            except TypeError as error:
                print(f"[ERROR] -> incomplete line: {pigeon_row}")