import random
import shutil
from pathlib import Path
from typing import List

my_path = r"C:\Demo"

#PART 1 : GET THE FOLDERS IN A SPECIFIC LOCATION
def get_directories(location : str, limit : int = 1000)->List[Path]:
    """
    returns list with all folders on a specific location
    """
    directories = []
    path:Path # generates intellisense
    for path in Path(location).rglob("*"):
        # print(path)
        if path.is_dir():
            directories.append(path)
        if len(directories) > limit:
            break
    return directories


print(len(get_directories(my_path)))

#PART 2 : GENERATE SOME FILES
def hack_my_system(location : str, hacker_name : str):
    """
    Find random folder at a specific location
    create txt-file in the folder
    """
    dirs = get_directories(location)
    secret_path = random.choice(dirs)

    filename = f"hacker_{random.randint(100, 200)}.txt"
    path = f"{secret_path}/{filename}"

    # print(path)
    with open(path, "w") as file:
        file.write(f"You have been hacked by {hacker_name}! :)")

for index in range(30):
    hack_my_system(my_path, "Anna-Kyra")

#PART 3: FIND THE HACKED FILES
def find_hacked_locations(location : str):
    """
    Looking for all files starting with hack
    move them to another folder
    """
    #aanmaken van directory "CLEANED"
    target_dir = Path("CLEANED")
    if not target_dir.exists():
        target_dir.mkdir()

    num_hacked = 0
    path:Path
    for path in Path(location).rglob("hack*.txt"):
        print(f"Hacker file found in {path.parent}")
        print(f"[FILENAME] {path.stem}")
        num_hacked += 1

        shutil.move(path, target_dir / f"{path.stem}{path.suffix}")
        print("-> cleaned")

    print(f"{num_hacked} files has been cleaned")

find_hacked_locations(my_path)