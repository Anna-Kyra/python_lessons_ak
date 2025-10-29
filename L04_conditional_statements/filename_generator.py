def clean_string(text: str) -> str:
    """
    :param text: the text to clean up
    :return: the cleaned up text
    """
    return f"{text
    .strip()
    .replace(" ","_")
    .replace("'", "")
    .replace("-", "_")
    }"

first_name = clean_string(input("What is your first name? "))
last_name = clean_string(input("What is your last name? "))
group_number = int(input("What is your group number? ")) #:02d

print("[0] Programming for artists\n"
      "[1] Compositing\n"
      "[2] Prepro")
course = int(input("Which course is this for? "))

if course == 0:
    lab_number = int(input("\nWhich lab is this? "))
    print(f"1DAE{group_number:02d}_"
       f"{last_name.title()}_"
       f"{first_name.title()}_"
       f"L{lab_number:02d}")
elif course == 1:
    project_code = input("\nEnter project code: ")
    version_number = int(input("Enter version number: "))
    print(f"{project_code}"
       f"_1vfx{group_number:02d}e_"
       f"{last_name.title()}_"
       f"{first_name.title()}_"
       f"v{version_number:03d}")
elif course == 2:
    project_name = input("\nWhat is the name of the project? ")
    print(f"{last_name.title()}_"
       f"{first_name.title()}_"
       f"1DAE{group_number:02d}_"
       f"{project_name}")