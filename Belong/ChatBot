print("Bot: Hello!")
print("Bot: I am your ChatBot")

def get():
    print("Bot: How can I help you with your tasks?")
    uinput = input("User: ")
    return uinput.lower().strip()

task = []
print()
while True:
    cmd = get()

    if cmd == "add task" or cmd == "add tasks":
        print('Bot: Please Provide Task Details, Type "QUIT" to stop adding tasks')
        while True:
            detail = input("User: ").lower().strip()
            if detail == "quit":
                break
            else:
                task.append(detail)

    elif cmd in ["task", "tdetail", "task details"]:
        if task:
            print("Bot: Here are your tasks:")
            print(*task, sep="\n")
        else:
            print("Bot: No tasks added yet.")

    elif cmd == "quit":
        print("Bot: GoodBye! Thank you!")
        break

    else:
        print("Bot: I didn't understand that command.")

print()