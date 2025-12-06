courses = ["Programming for artists", "Applied Math and Physics Fundamentals", "Preproduction", "3D1", "Compositing",
           "Programming for artists", "Foundation for film", "Foundation for games", "Compositing", "3D1"]
collection = set(courses)
collection_list = list(collection)
collection_list.sort()

for index, course in enumerate(collection_list):
    print(f"[{index}] {course}")

course_number = int(input("Select a course number: "))
print(f"\t-> You have chosen {collection_list[course_number].upper()}")