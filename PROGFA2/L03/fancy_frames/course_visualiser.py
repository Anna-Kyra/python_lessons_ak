from ascii_frame import AsciiFrame

course_chapters = {
    "Python Basics": ["Introduction", "Variables and Data Types", "Control Flow", "Functions"],
    "3D Modeling": ["Introduction to 3D", "Meshes and Textures", "Lighting and Rendering"],
    "Environment Design": ["Concept Art for Environments", "Lighting in Environments"],
    "Digital Sculpting": ["Sculpting Tools Overview", "Anatomy for Artists", "Character Design", "Texturing and Shading"],
}

title = AsciiFrame("Hello student, welcome to this course!", "~")
print(f"{title}\n")



for title, chapters in course_chapters.items():
    title = AsciiFrame(title)
    print(title)
    for index, chapter in enumerate(chapters, start=1):
        chapter_name = f"Chapter {index}: {chapter}"
        chapter = AsciiFrame(chapter_name,"-", 1)
        print(chapter)