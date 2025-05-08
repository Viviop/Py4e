import json

print("Bot: Hello!")
print("Bot: I am your ChatBot")

def get():
    print("Bot: How can I help you with your tasks?")
    uinput = input("User: ")
    return uinput.lower().strip()

tasks = []
print()

while True:
    cmd = get()

    if cmd == "add task" or cmd == "add tasks":
        print('Bot: Let\'s add a task. Type "QUIT" at any time to stop adding.')

        while True:
            print("Bot: Enter subject:")
            subject = input("User: ").strip()
            if subject.lower() == "quit":
                break

            print("Bot: Enter description:")
            description = input("User: ").strip()
            if description.lower() == "quit":
                break

            print("Bot: Enter deadline (e.g., 28-08-2025):")
            deadline = input("User: ").strip()
            if deadline.lower() == "quit":
                break

            print("Bot: Is it completed? (yes/no)")
            status_input = input("User: ").strip().lower()
            if status_input == "quit":
                break
            status = True if status_input in ["yes", "y"] else False

            # Create structured task dictionary
            task = {
                "Subject": subject,
                "Description": description,
                "Deadline": deadline,
                "Completion Status": status
            }

            tasks.append(task)
            print("Bot: Task added!\n")

    elif cmd in ["task", "tdetail", "task details"]:
        if tasks:
            print("Bot: Here are your tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        else:
            print("Bot: No tasks added yet.")

    elif cmd == "quit":
        print("Bot: Saving your tasks to homework_data.json...")
        with open("homework_data.json", "w") as file:
            json.dump(tasks, file, indent=4)
        print("Bot: Goodbye! Thank you!")
        break

    else:
        print("Bot: I didn't understand that command.")

print()
