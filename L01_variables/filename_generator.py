first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
major = input("What major are you in (GGP, VFX, ANI,...)? ")
group_number = int(input("What is your group number? ")) #:02d
group_language = input("Are you in the English (E) or Dutch (N) group? ")
course_abbreviation = input("Which course is this for (abbreviation, e.g. PROFA1)? ")
assignment_name = input("What is the name of the assignment? ")

result = print(f"{course_abbreviation.upper()}_2526_{major.capitalize()}{group_number:02d}{group_language.capitalize()}_{first_name.capitalize()}_{last_name.capitalize()}_{assignment_name.capitalize()}")