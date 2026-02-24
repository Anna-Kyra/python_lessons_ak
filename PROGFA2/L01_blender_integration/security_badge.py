# SECURITY BADGE
id_set = {101, 105, 220, 440, 220, 101, 952}

print(f"We authorize {len(id_set)} id's.")
badge_number = int(input("Please enter your badge number: "))
print(f"=> Attempted bage: {badge_number}")

if badge_number in id_set:
    print("=> ACCESS GRANTED!")
else:
    print("X INTRUDER ALERT!")