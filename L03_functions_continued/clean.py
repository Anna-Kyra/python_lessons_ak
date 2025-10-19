def clean_string(text: str) -> str:
    """
    Cleans up any text to use in a filename:
    - removes any trailing / leading spaces (E.g. "  George   " becomes "George")
    - replaces inner spaces by an underscore _ (E.g. "Van Diesel" becomes "Van_Diesel")
    - removes any quotes ' in the text (O'Conner becomes OConner)
    - replaces all hyphens - by an underscore _ (E.g. "Jean-Claude" becomes "Jean_Claude")
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
major = clean_string(input("What major are you in (GGP, VFX, ANI,...)? "))
group_number = int(input("What is your group number? ")) #:02d
group_language = clean_string(input("Are you in the English (E) or Dutch (N) group? "))
course_abbreviation = clean_string(input("Which course is this for (abbreviation, e.g. PROGFA1)? "))
assignment_name = clean_string(input("What is the name of the assignment? "))

print(f"{course_abbreviation.upper()}"
       f"_2526_{major.upper()}"
       f"{group_number:02d}"
       f"{group_language.title()}_"
       f"{first_name.title()}_"
       f"{last_name.title()}_"
       f"{assignment_name.title()}")