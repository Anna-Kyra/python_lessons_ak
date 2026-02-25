from person import Person

family = list()
father = Person("de Jong", "John", 60)
mother = Person("de Jong", "Angelina", 62)
kid = Person("de Jong", "Jantje", 6)

family.append(father)
family.append(mother)
family.append(kid)

for member in family:
    print(member)
