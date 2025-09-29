name_left = input("The person sitting to my left is called ")
country_left = input(f"{name_left} is from ")
age_left = int(input(f"The age of {name_left} from {country_left} is "))

name_right = input("The person sitting to my right is called ")
country_right = input(f"{name_right} is from ")
age_right = int(input(f"The age of {name_right} from {country_right} is "))

average_age = (age_left + age_right) / 2
print(f"The average age of {name_left} and {name_right} is {average_age}.")