import ct
f="RIDA"
print("1. You can add a task")
print("2. You can view added tasks")
print("3. You can greet the bot by saying Hello/Hi")
print("4. You can tell you name and ask its name")
print("5. You can ask the bot to tell you a joke by saying - Tell me a joke")
print("6. You can ask how it is doing")
print("7. You can say Bye or See you or Exit to end the current conversation and come back later by saying RIDA")


while f=="RIDA":
    a="y"
    while a=="y":
        c=input("Greetings! How may I help you today? ")
        if ("add" in c.lower()) and ("task" in c.lower()):
            ct.add_homework()
        elif ("view" in c.lower()) and ("tasks" in c.lower()):
            ct.view_homework()
        elif ("mark" in c.lower()) and ("tasks" in c.lower()):
            ct.mark_homework()
        elif ("hello" in c.lower()) or ("hi" in c.lower()):
            print("Hello there! How do you do?")
        elif ("name" in c.lower()) and ("?" not in c.lower()):
            h=c.strip()
            L1=h.split()
            e=L1[len(L1)-1]
            print("Hi",e,". So nice to meet you!")
        elif ("name" in c.lower()) and ("?" in c.lower()):
            print("My name is RIDA")
        elif ("joke" in c.lower()) and ("?" not in c.lower()):
            print("Sure, here you go")
            print("Why don't scientists trust atoms? Because they make up everything!")
        elif "you?" in c.lower() or "you ?" in c.lower():
            print("Although I am just a software, I am doing great? What about you?")
        elif ("bye" in c.lower()) or ("bye-bye" in c.lower()) or ("see you" in c.lower()) or ("exit" in c.lower()):
            print("Ok bye. It was nice talking to you. Let me know if you need anything else! ")
            break
        else:
            print("I don't have answer to that as of now.....")
        
        
        a=input("To talk more, enter y each time: ")
    print("Conversation ended")
    f=input("Enter 'RIDA' if you want to talk again: ")
print("No more talking!! RIDA is busy.....")




