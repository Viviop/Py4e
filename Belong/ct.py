import json


homework_tasks = [
    {
        "Subject": "Math",
        "Description": "Complete exercises from page 45 to 48",
        "Deadline": "Tomorrow",
        "Completion Status": "Incomplete"
    },
    {
        "Subject": "English",
        "Description": "Write a 500-word essay on Shakespeare's tragedies",
        "Deadline": "Next week",
        "Completion Status": "Completed"
    },
    {
        "Subject": "Science",
        "Description": "Prepare a presentation on renewable energy",
        "Deadline": "Next month",
        "Completion Status": "Completed"
    }
]

with open("botready.json", 'w') as file:
    json.dump(homework_tasks, file, indent=4)

def load_homework():
    try:
        with open("botready.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_homework(tasks):
    with open("botready.json", 'w') as file:
        json.dump(tasks, file, indent=4)

def view_homework(): #available in bot
    tasks = load_homework()
    if not tasks:
        print("No homework tasks found.")
    else:
        print("Here are the tasks: ")
        for i in tasks:
            print(i)
            print()
def mark_homework(): #available in bot
    tasks=load_homework()
    z=eval(input("Enter task to be marked"))
    if not tasks:
        print("No homework tasks found.")
    else:
        for i in tasks:
            if i==z:
                if (i['Completion Status']=="Completed"):
                    print("Already completed")
                    break
                else:
                    i['Completion Status']="Completed"
                    save_homework(tasks)
                    print("Marked")
                    break
        else:
            print("No such task found")
        

def add_homework(): #available in bot
    tasks = load_homework()
    subject=input("Enter subject: ")
    description = input("Enter description: ")
    deadline = input("Enter deadline: ")
    completed = input("Enter status: ")
    task = {
        "Subject": subject,
        "Description": description,
        "Deadline": deadline,
        "Completion Status": completed
    }
    tasks.append(task)
    save_homework(tasks)
    print("Task added.")




