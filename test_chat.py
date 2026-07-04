from services.conversation import chat

while True:
    msg = input("You: ")

    if msg == "exit":
        break

    print(chat(msg))