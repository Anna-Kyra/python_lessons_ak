from task import Task
import random

todos = [
    "Finish progfa assignments",
    "Optimize mesh",
    "Bake normals",
    "Rig character",
    "Export to engine",
    "Eat pizza",
    "Submit before deadline",
    "Script a tool",
    "Try to stay awake",
    "Fix weird shading",
    "Cry over topology",
    "Forget to save",
    "Crash at 99% bake",
    "Drink more coffee"
]

t = Task("my first task")

my_tasks : list[Task] = []


def make_tasklist():
    for todo in todos:
        new_task = Task(todo)
        my_tasks.append(new_task)
        if random.randint(0, 1)%2==0:
            new_task.is_finished = True

def print_tasklist():
    for task in my_tasks:
        print(task)

def print_todolist():
    print("----- TO DO -----")
    for task in my_tasks:
        if not task.is_finished:
            print(task)


make_tasklist()
print_tasklist()
print_todolist()