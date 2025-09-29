nameLeft = input("The person sitting to my left is called ")
countryLeft = input(f"{nameLeft} is from ")
ageLeft = int(input(f"The age of {nameLeft} from {countryLeft} is "))

nameRight = input("The person sitting to my right is called ")
countryRight = input(f"{nameRight} is from ")
ageRight = int(input(f"The age of {nameRight} from {countryRight} is "))

averageAge = (ageLeft + ageRight) / 2
print(f"The average age of {nameLeft} and {nameRight} is {averageAge}.")