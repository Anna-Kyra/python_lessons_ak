#Slice of life
print("-----------------------Welcome to---------------------------\n"
      "░▀█▀░█░█░█▀▀░░░█▀█░█▀▄░█▀▀░█▀▀░█▀█░█▀█░░░▀█▀░█▀▄░█▀█░▀█▀░█░░\n"
      "░░█░░█▀█░█▀▀░░░█░█░█▀▄░█▀▀░█░█░█░█░█░█░░░░█░░█▀▄░█▀█░░█░░█░░\n"
      "░░▀░░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░░▀░░▀░▀░▀░▀░▀▀▀░▀▀▀\n"
      "--------------------------------------------------------------\n"
      "Press enter to continue_ \n")
input()

# Profession
print("Many types of people made the trip to Oregon.\n")
profession = input("What's your profession? ")
print("--------------------------------------------------------------\n")

#Names
leader = input("What is the first name of the wagon leader? ")
person2 = input("What is the first name of the passenger princess? ")
person3 = input("What is the first name of the third person who came along? ")
print("--------------------------------------------------------------\n")

#Month
month = input("It is 1848. Your jumping off place for Oregon is Independence, Missouri.\n"
              "You must decide which month to leave Independence: ")
print(f"{month.capitalize()}, really? Uhmm oke...\n"
      f"You will begin you journey at {month.capitalize()} 1, 1848.")
print("Press enter to continue_ \n")
input()
print("--------------------------------------------------------------\n")

#Money
money = 1600.00
print("Before leaving Independence you should buy equipment and supplies. "
      f"You have ${money} in cash.\n\n")

#Horse
print(f"You first find a cute stable that sells horses. It looks a bit sketchy, but you go in anyway.\n"
      f"Choose a horse:\n"
      f"1. Pedro   (fastest horse ever lived) -- $1200.00\n"
      f"2. Henk    (he's doing his job) -------- $ 500.00\n"
      f"3. Alberta (she's a bit..too old) ------ $ 80.00\n")
horse_name = input("What horse will you pick for your journey? (type in a name) ")

print(f"Oops, apparently it was a scam and they took all your money. You are broke now, but hey you got a cool new horse named {horse_name.capitalize()} now.")
money = 0.00
print("Press enter to continue_ \n")
input()
print("--------------------------------------------------------------\n")

#Food
print(f"[{month.capitalize()} 2, 1848]\n"
      "You follow your way to oregon, but got lost because you couldn't afford to buy a map anymore\n"
      f"'{person2.capitalize()}' decided to find something to eat, because everyone started to get hungry.\n")
food = input(f"'{person2.capitalize()}' found some 'berries' and 'mushrooms'!\n "
      f"Because you are the leader they asked you what she may eat: ")
print(f"Apperently it turned out that the {food} were highly poisonous.\n"
      f"Your {profession} job couldn't have prepared you enough to handle this situation.\n"
      f"'{person2.capitalize()}' sadly died of poison.\n\n"
      "\tCause of death: poison\n")
print("Press enter for a minute of silence_ \n")
input()
print("--------------------------------------------------------------\n")

#lost
print(f"[{month.capitalize()} 10, 1848]\n"
      "A few days past and you still have you idea where you are.\n"
      f"You managed to get some food, but it wasn't all that nutritious. "
      f"You're belly is feeling weird for awhile now, but you decided to ignore it for {person3}'s sake.\n"
      f"'{person3.capitalize()}' burned himself while making a fire a few days ago. It looks very infected and they have a fever.")
print("Press enter to continue_ \n")
input()
print("--------------------------------------------------------------\n")

#infection
print(f"[{month.capitalize()} 20, 1848]\n"
      f"'{person3.capitalize()}' sadly passed away in his sleep.\n\n"
      "\tCause of death: infection\n")
print("Press enter to continue_ \n")
input()
print("--------------------------------------------------------------\n")

#Dysentary
print(f"[{month.capitalize()} 30, 1848]\n"
      f"Your bloody diarrhea tells you that your end is near. At your final moment you think about '{person2.capitalize()}' and '{person3.capitalize()}' while you are petting your horse {horse_name}.\n\n")
print("\tCause of dead: dysentery\n")
print("Press enter to credits_ \n")
input()
print("--------------------------------------------------------------\n")

print("Credits: The Oregon Trail - Don Rawitsch, 1971")